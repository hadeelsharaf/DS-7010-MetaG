import streamlit as st
import plotly.express as px
from common import transform_fungi_data, tidy_fungi_data

df_fungi=transform_fungi_data()
# transform column 'Italy_MM_bulk soil_no straw' to binary by rplacing '+' with 1 and '-' with 0 
df_fungi['Italy_MM_bulk soil_no straw'] = df_fungi['Italy_MM_bulk soil_no straw'].replace({'+': 1, '-': 0})


path_columns = df_fungi.columns.values[0:5]
fig = px.sunburst(df_fungi, path=path_columns, values='Italy_MM_bulk soil_no straw')
st.header('Fungi Sunburst Chart')
st.write(""" The sunburst chart is applied to the Fungi data before tidying the data. 
         The sunburst chart is used to visualize the Fungi data taxonomy .""")

st.plotly_chart(fig)


df_fungi_tidy=tidy_fungi_data()
histo_fig = px.histogram(df_fungi_tidy, x='value', color='location', histfunc='count', facet_col='treatment')
st.header('Fungi Histogram Chart after tidying the data')
st.write(""" The histogram chart is applied to the Fungi data after tidying the data. 
         The histogram chart is used to visualize the Fungi data distribution over location .""")
st.plotly_chart(histo_fig)
