import streamlit as st
import plotly.subplots as sp
import plotly.graph_objects as go


st.title('Experimental Visualization')
st.write("""This page is for experimental visualization as proof of concept that charts can be paginated. 
         The chart below is a bar chart that is paginated. The chart is paginated because it has more than 4 labels and binary values. 
         The chart is paginated to make it easier to read.""")
# Sample data
labels = ['Label1', 'Label2', 'Label3', 'Label4', 'Label5', 'Label6', 'Label7', 'Label8', 'Label9', 'Label10', 'Label11', 'Label12', 'Label13', 'Label14', 'Label15', 'Label16', 'Label17', 'Label18', 'Label19', 'Label20']
values = [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,1, 0, 0 ]

# Number of labels per page
labels_per_page = 4

# Calculate the number of pages needed
num_pages = -(-len(labels) // labels_per_page)  # Ceiling division to get the total number of pages

# Create subplots
fig = sp.make_subplots(rows=num_pages, cols=1, subplot_titles=[f'Page {i+1}' for i in range(num_pages)])

# Populate each subplot with data
for page in range(num_pages):
    start_idx = page * labels_per_page
    end_idx = (page + 1) * labels_per_page
    current_labels = labels[start_idx:end_idx]
    current_values = values[start_idx:end_idx]

    # Create horizontal bar chart for the current page
    trace = go.Bar(x=current_labels, y=current_values,  name=f'Page {page+1}')
    fig.add_trace(trace, row=page+1, col=1)

# Update layout
fig.update_layout(
    height=num_pages * 100,  # Adjust the height based on the number of pages
    showlegend=False,  # Hide legend for simplicity
    title_text='Pagination Example',
     yaxis=dict(title='Value',tickmode='linear',
        tick0=0,
        dtick=1)
)

# Show the plot
st.plotly_chart(fig)
