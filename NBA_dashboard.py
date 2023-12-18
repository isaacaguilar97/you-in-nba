import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import statistics

# Load Data
final_df = pd.read_csv('data/final_table.csv')

# App Title
st.title('Your spot in the NBA')

# Description
st.markdown('Imagine you where an NBA player. What position would you like to be? What skills would you need to have based on your position and hieght. If you ever have wondered these questions or would like to just improve your game through some benchmarks that help you know what your skills should look like to be an above average baller, this app is for you. Hope you enjoy it.')

# Warning message the results are comming from a sample of NBA players from 2023 season

# Header 1
st.header('Explore the Positions')

# Position Input
pos1 = st.selectbox("Select Position", final_df['pos'].unique().tolist())
# Have one selected by default or prompt to select one (Make it required)

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
fig = px.histogram(strengths_df, x='b_strength', title=p_n[pos1], labels={'b_strength': '', 'count': 'Count'}, color_discrete_sequence=px.colors.qualitative.Set2)
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
#pos2 = col3.selectbox("Role", final_df['pos'].unique().tolist())
perf = col3.selectbox("Select Performance", final_df[final_df['pos'] == pos1]['performance'].unique().tolist())
height = col4.number_input('Enter you Height in Meters')


# Filter position and performance
result_df = final_df[(final_df['pos'] == pos1) & (final_df['performance'] == perf)]

# Group by hieght
result_df = final_df.groupby(['height_m']).agg({
    'points': 'mean',
    'min': 'mean',
    'fgp': 'mean',
    'ftp': 'mean',
    'tpp': 'mean',
    'totReb': 'mean',
    'assists': 'mean',
    'steals': 'mean',
    'blocks': 'mean',
    'b_strength': lambda x: statistics.mode(x).mode[0]
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

# Filter by height
skills = find_closest_height(result_df, 2.2, tolerance=0.01)

# Remove height column and make table vertical
skills = skills.drop('height_m', axis=1).T

# Rename column
skills.rename(columns={skills.columns[0]: 'Average Value per Game'}, inplace=True)

# Show table
st.dataframe(skills)
#