# pages/bac_data.py
import streamlit as st
import pandas as pd
from common import transform_bacteria_data, tidy_bacteria_data

df_bacteria = transform_bacteria_data()
df_bacteria_tidy = tidy_bacteria_data()

st.title('Bacteria Data before tidying:')
st.dataframe(df_bacteria)

st.title('Bacteria Data After tidying:')
st.dataframe(df_bacteria_tidy)