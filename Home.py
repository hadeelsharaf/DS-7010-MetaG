# main.py
import streamlit as st
st.set_page_config(
    page_title="Home Page",
    page_icon="📊",
) 
st.title("META-Gen")



st.write('''
         ## Welcome to META-Gen visualization tool! 
         
         This tool is designed to visualize dataset from the study of the effect of straw treatments on the microbial community in the soil.         
         Packages used in this application are: streamlit, pandas, numpy, plotly, and matplotlib.
         Clutering and data transformation are done using pandas, numpy and k-protoypes algorithm.
         
         ## The application is divided into 4 sections:
        
          1. Bacteria Data View
         
          2. Bacteria Data Visualization charts
         
          3. Fungi Data View
         
          4. Fungi Data Visualization charts

         ''')


