# pages/bac_data.py
import streamlit as st
import pandas as pd
from common import transform_bacteria_data, tidy_bacteria_data

df_bacteria = transform_bacteria_data()
df_bacteria_tidy = tidy_bacteria_data()

st.header('Bacteria Data before tidying:')
st.dataframe(df_bacteria)

st.header('Bacteria Data after tidying:')
st.dataframe(df_bacteria_tidy)