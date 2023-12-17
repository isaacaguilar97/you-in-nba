import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

# Load Data
final_df = pd.read_csv('data/final_table.csv')

# App Title
st.title('Your spot in the NBA')

# Description
st.text('This is an example of what my description will look like once it has data inside of it. Lets go!')

# Header 1
st.header('Explore the Positions')

# Position Input
pos1 = st.selectbox("Select Position", final_df['pos'].unique().tolist())
# Have one selected by default or prompt to select one (Make it required)

# Filter data
strengths_df=final_df[final_df['pos'] == pos1]

# Show barplot
fig = px.histogram(strengths_df, x='b_strength', title='Point Forward', labels={'b_strength': '', 'count': 'Count'})
st.plotly_chart(fig)

# Height Range
Min = strengths_df['height_m'].min()
Max = strengths_df['height_m'].max()
col1, col2 = st.columns(2)
col1.metric(label="Minumum Height", value=Min)
col2.metric(label="Maximum Height", value=Max)

# Average of Minutes played in a game
st.write(f"The average of minutes on the court is: {round(final_df['min'].mean())}")

# Add position and stats descriptions at the left of the dashboard ###

col1, col2, col3 = st.columns(3)
height = col1.number_input('Enter you Height in Meters')
pos2 = col2.selectbox("Select Position", final_df['pos'].unique().tolist())
performance = col3.selectbox("Select Performance", final_df['performance'].unique().tolist())

# Create Dataframe and display it
#st.dataframe(top_names)