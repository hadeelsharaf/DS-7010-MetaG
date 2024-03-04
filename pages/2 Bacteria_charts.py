import streamlit as st
import plotly.express as px
from common import transform_bacteria_data, tidy_bacteria_data

df_bacteria=transform_bacteria_data()
df_bacteria['Italy_MM_bulk soil_no straw'] = df_bacteria['Italy_MM_bulk soil_no straw'].replace({'+': 1, '-': 0})
path_columns = df_bacteria.columns.values[0:6]
fig = px.sunburst(df_bacteria, path=path_columns, values='Italy_MM_bulk soil_no straw')
st.header('Bacteria Sunburst Chart')
st.write(""" The sunburst chart is applied to the bacteria data before tidying the data. 
         The sunburst chart is used to visualize the bacteria data taxonomy .""")

st.plotly_chart(fig)

