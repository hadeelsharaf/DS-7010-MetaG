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
    height=num_pages * 100, 
    showlegend=False,  # Hide legend for simplicity
    title_text='Paginating Bar Chart',
     yaxis=dict(title='Value',tickmode='linear',
        tick0=0,
        dtick=1)
)

st.header('Paginated bar chart')
# Show the plot
st.plotly_chart(fig)


# experimental visualization 


# Sample data
labels = ['Label1', 'Label2', 'Label3', 'Label4', 'Label5', 'Label6', 'Label7']
values = [1, 1, 0, 0, 1, 0, 1, 0,]

# Create a bar chart
fig2 = go.Figure()

for i, (label, value) in enumerate(zip(labels, values)):
    color = 'green' if value == 1 else 'white'
    border_color = 'black'
    
    fig2.add_shape(
        type='rect',
        x0=i,
        y0=0,
        x1=i + 1,
        y1=1,
        fillcolor=color,
        line=dict(color=border_color),
        opacity=1
    )

# Update layout
fig2.update_layout(
    xaxis=dict(tickvals=list(range(len(labels))), ticktext=labels),
    yaxis=dict(range=[0, 1]),
    showlegend=False,
)

# Show the plot
st.header('Experimental Visualization for binary values')
st.plotly_chart(fig2)
