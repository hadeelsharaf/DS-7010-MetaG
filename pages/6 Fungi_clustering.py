# to contain dendrogram of the fungi clustering
# to contain dendrogram of the fungi clustering
import streamlit as st
from scipy.spatial import distance_matrix
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
import kmodes.kprototypes as kprototypes

import numpy as np

from common import tidy_fungi_data

df_fungi = tidy_fungi_data()

# st.set_option('deprecation.showPyplotGlobalUse', False)

def create_dm(dataset):
    #if the input dataset is a dataframe, we take out the values as a numpy. 
    #If the input dataset is a numpy array, we use it as is.
    if type(dataset).__name__=='DataFrame':
        dataset=dataset.values    
    lenDataset=len(dataset)
    distance_matrix=np.zeros(lenDataset*lenDataset).reshape(lenDataset,lenDataset)
    for i in range(lenDataset):
        for j in range(lenDataset):
            x1= dataset[i].reshape(1,-1)
            x2= dataset[j].reshape(1,-1)
            distance=kprototypes.matching_dissim(x1, x2)
            distance_matrix[i][j]=distance
            distance_matrix[j][i]=distance
    return distance_matrix
data=df_fungi.iloc[:, :6]
data=data.drop_duplicates()
data.set_index('Genus', inplace=True)
distance_matrix=create_dm(data)
linkage_matrix = linkage(distance_matrix, "ward")
plt.figure(figsize=(12, 12))
dendrogram(linkage_matrix, labels=data.index,leaf_font_size=8, leaf_rotation=90.)
st.header('Fungi Dendrogram')
st.write(""" The dendrogram is applied to the fungi data after tidying the data. 
            The dendrogram is used to visualize the fungi data clustering using ward method.""")

with st.container():
    plt.title("matplotlib.pyplot : Dendrogram Using ward Linkage")
    #plt.xticks(rotation='vertical')
    
    st.pyplot(plt.show())

st.write(":heavy_minus_sign:" * 32)
st.header('Fungi Dendrogram singel method')

linkage_matrix = linkage(distance_matrix, "single")
plt.figure(figsize=(12, 12))
dendrogram(linkage_matrix, labels=data.index,leaf_font_size=8, leaf_rotation=90.)
with st.container():
    plt.title("matplotlib.pyplot : Dendrogram Using single Linkage")

    st.pyplot(plt.show())
