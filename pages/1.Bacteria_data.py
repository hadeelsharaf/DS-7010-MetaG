# pages/bac_data.py
import streamlit as st
import pandas as pd
from common import get_bacteria_df

df_bacteria = get_bacteria_df()

st.title('Bacteria Data')
st.dataframe(df_bacteria)