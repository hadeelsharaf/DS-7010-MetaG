import streamlit as st
import plotly.express as px
from common import transform_bacteria_data, tidy_bacteria_data

df_bacteria=transform_bacteria_data()
df_bacteria['Italy_MM_bulk soil_no straw'] = df_bacteria['Italy_MM_bulk soil_no straw'].replace({'+': 1, '-': 0})
df_bacteria['Italy_MM_bulk soil_straw'] = df_bacteria['Italy_MM_bulk soil_straw'].replace({'+': 1, '-': 0})

path_columns = df_bacteria.columns.values[0:6]
fig = px.sunburst(df_bacteria, path=path_columns, values='Italy_MM_bulk soil_no straw')
st.header('Bacteria Sunburst Chart')
st.write(""" The sunburst chart is applied to the bacteria data before tidying the data. 
         The sunburst chart is used to visualize the bacteria data taxonomy .""")
         

st.plotly_chart(fig)

# Convert the columns to the same data type (e.g., float)
df_bacteria['Italy_MM_bulk soil_straw'] = df_bacteria['Italy_MM_bulk soil_straw'].astype(int)
df_bacteria['Italy_MM_bulk soil_no straw'] = df_bacteria['Italy_MM_bulk soil_no straw'].astype(int)

bar_fig = px.bar(df_bacteria, x='Genus', y=['Italy_MM_bulk soil_straw', 'Italy_MM_bulk soil_no straw'], title='Italy Bulk soil with MM rotation')
bar_fig.update_layout(legend_title_text='Italy Bulk Soil')
bar_fig.update_xaxes(title_text='Genus')
bar_fig.update_yaxes(title_text='Value')

st.header('Bacteria counts before tidying the data')
st.plotly_chart(bar_fig)

df_bacteria_tidy=tidy_bacteria_data()
histo_fig = px.histogram(df_bacteria_tidy, x='value', color='location', histfunc='count', facet_col='treatment')
st.header('Bacteria Histogram Chart after tidying the data')
st.write(""" The histogram chart is applied to the bacteria data after tidying the data. 
         The histogram chart is used to visualize the bacteria data distribution .""")
st.plotly_chart(histo_fig)


df_positive = df_bacteria_tidy[df_bacteria_tidy['value'] == '+']

df_counts = df_positive.groupby('Genus')['value'].size()#.reset_index(name='counts')

st.header('Counts of tidy values grouped by genus')
# bar chart for the counts of values grouped by genus
bar_fig = px.bar(df_counts, x=df_counts.index, y='value', labels={'value': 'Counts', 'index': 'Genus'})
st.plotly_chart(bar_fig)