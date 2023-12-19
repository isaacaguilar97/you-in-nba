import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from statistics import mode

# Load Data
final_df = pd.read_csv('data/final_table.csv')

# Prep Abbreviation table
abb = {
    'Metric': ['points', 'mins', 'fgp', 'ftp', 'tpp', 
               'totReb', 'assists', 'pFouls', 'steals', 'turnovers', 'blocks', 'plusMinus'],
    'Description': [
        'Points scored per game.',
        'Minutes played per game.',
        'Percentage of field goals made.',
        'Percentage of free throws made.',
        'Percentage of three-pointers made.',
        'Total number of rebounds.',
        "Number of passes leading to a teammate's score.",
        'Personal fouls committed.',
        'Number of times the player takes the ball from an opponent.',
        'Number of times the player loses possession of the ball.',
        'Number of times the player deflects or stops a field goal attempt by an opponent.',
        'Point differential when the player is on the court.'
    ]
}

with st.sidebar:
    # App Title
    st.title('Your spot in the NBA')

    # Description
    st.markdown('Imagine you where an NBA player. What position would you like to be? What skills would you need to have based on your position and hieght. If you ever have wondered these questions or would like to just improve your game through some benchmarks that help you know what your skills should look like to be an above average baller, this app is for you. Hope you enjoy it.')

    # Position Input
    pos1 = st.selectbox("Select Position", final_df['pos'].unique().tolist())
    
    # Warning message
    st.info("Be aware that results come from a sample of NBA players from season 2023")

    # Abbreviations
    with st.expander("Abbreviation Index"):
        st.table(abb)

# Header 1
st.header('Explore the Positions')

# Positions Dictionary
p_n = {
    'PF': 'Power Forward',
    'SG': 'Shooting Guard',
    'C': 'Center',
    'PG': 'Point Guard',
    'SF': 'Small Forward',
    'F': 'Forward',
    'G': 'Guard'
}

# Filter data
strengths_df=final_df[final_df['pos'] == pos1]

# Show barplot
fig = px.histogram(strengths_df, x='b_strength', title=f'{p_n[pos1]} Skills', labels={'b_strength': '', 'count': 'Players Count'}, color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig)

#Divide in to columns
col1, col2 = st.columns(2)

# Show metrics ##
# Height Range
Min = strengths_df['height_m'].min()
Max = strengths_df['height_m'].max()
col1.metric(label="Height Range in meters:", value=f'{Min} - {Max}')
# Average of Minutes played in a game
col2.metric(label="Average minutes on the Court", value=round(strengths_df['min'].mean()))


##### Header 2 #####
st.header('What kind of NBA player would you be?')

# DESCRIPTION
st.markdown('Now that you have idenitfied what position you like the most, explore the skills you would need to have based on that position, your desired perfomance and your height.')

#Input
col3, col4 = st.columns(2)
perf = col3.selectbox("Select Performance", final_df[final_df['pos'] == pos1]['performance'].unique().tolist())
height = col4.slider('Select your height', min_value=1.5, max_value=2.2, value=1.75, step=0.01)

# Filter position and performance
result_df = final_df[(final_df['pos'] == pos1) & (final_df['performance'] == perf)]

# Group by hieght
result_df = result_df.groupby(['height_m']).agg({
    'points': 'mean',
    'min': 'mean',
    'fgp': 'mean',
    'ftp': 'mean',
    'tpp': 'mean',
    'totReb': 'mean',
    'assists': 'mean',
    'steals': 'mean',
    'blocks': 'mean',
    'b_strength': lambda x: mode(x)
}).reset_index()

# Function that find closest height and outputs a filtered table with that height
def find_closest_height(df, target_height=1.77, tolerance=0.01):
    # Check if the target height is present in the DataFrame
    if target_height in df['height_m'].values:
        return df[df['height_m'] == target_height]
    
    # If not, find the closest height within the specified tolerance
    lower_height = target_height - tolerance
    upper_height = target_height + tolerance
    
    # Check if there are observations for the lower and upper heights
    lower_obs = df[(df['height_m'] >= lower_height) & (df['height_m'] <= target_height)]
    upper_obs = df[(df['height_m'] <= upper_height) & (df['height_m'] >= target_height)]
    
    # If both lower and upper observations are empty, and target_height is greater than max height, handle it
    if lower_obs.empty and upper_obs.empty:
        max_height = df['height_m'].max()
        if target_height > max_height:
            return df[df['height_m'] == max_height]
        else:
            return find_closest_height(df, target_height + 0.01, tolerance)
    
    # If either lower or upper observations are not empty, return the one with observations
    if not lower_obs.empty:
        return lower_obs
    else:
        return upper_obs

if height is None:
    st.write('Enter your Height')
else:
    # Filter by height
    skills = find_closest_height(result_df, height, tolerance=0.01)

    # Round up the values in the specified columns
    columns_to_round_up = ['points', 'min', 'totReb', 'assists', 'steals', 'blocks']
    skills[columns_to_round_up] = np.ceil(skills[columns_to_round_up])

    #Round to to decimal values
    columns_to_round_up = ['fgp', 'ftp', 'tpp']
    skills[columns_to_round_up] = round(skills[columns_to_round_up], 2)

    # Remove height column and make table vertical
    skills = skills.drop('height_m', axis=1).T

    # Rename column
    skills.rename(columns={skills.columns[0]: 'Average Value per Game'}, inplace=True)

    # Show table
    st.table(skills)

with st.expander("Explore a little more"):
##### Data Information #####
    st.header('Interesting Data Insights')

    # Position Count
    pos_counts = final_df['pos'].value_counts().reset_index()
    pos_counts.columns = ['Position', 'Frequency']
    fig2 = px.bar(pos_counts, x='Position', y='Frequency', labels={'Position': 'Positions', 'Frequency': 'Frequency'}, 
                title='Position Count', color_discrete_sequence=px.colors.sequential.Viridis)
    st.plotly_chart(fig2)

    # Biggest Strengths Distribution per Position
    fig3 = px.box(final_df, x='pos', y='height_m',
             color='pos',
             labels={'pos': 'Position', 'height_m': 'Height (meters)'},
             title='Boxplot of Height per Position')
    st.plotly_chart(fig3)

    # Biggest Strengths Distribution per Position
    fig4 = px.box(final_df, x='height_m', y='b_strength',
             color='b_strength',
             labels={'height_m': 'Height', 'b_strength': 'Biggest Strength'},
             title='Boxplot of Height per Biggest Strength')
    st.plotly_chart(fig4)

    # Points vs Performance
    fig5 = px.scatter(final_df, x='plusMinus', y='points', title='Scatter Plot of Points vs Performance',
                    labels={'plusMinus': 'Performance', 'points': 'Points'})
    st.plotly_chart(fig5)

# Final Words
st.markdown('Hope you enjoyed this dashboard, and were able to learn a little more about NBA players and yourself. If you want to learn more about the code I used for this dashboard, you can got to my [GitHub Repository](https://github.com/isaacaguilar97/you-in-nba). You can also go to learn more about the Exploratory Data Analysis that helped me build this Dashboard with my article in my Blog called [My NBA Exploratory Data Analysis](https://isaacaguilar97.github.io/my-blog/My-NBA-Exploratory-Data-Analysis)')

st.write('Thank you for exploring this Data with me. Now you know what it will take you to become an NBA player! :basketball: You can do it!')