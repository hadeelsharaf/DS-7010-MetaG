# pages/bac_data.py
import streamlit as st
import pandas as pd
from common import transform_fungi_data, tidy_fungi_data

df_fungi = transform_fungi_data()
df_fungi_tidy = tidy_fungi_data()

st.header('Fungi Data before tidying:')
st.dataframe(df_fungi)

st.header('Fungi Data after tidying:')
st.dataframe(df_fungi_tidy)