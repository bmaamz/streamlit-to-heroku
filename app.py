import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Component Knowledge Tracker')
st.header('Component Knowledge Tracker')
st.subheader('--Demo--')

### --- LOAD DATAFRAME
excel_file = 'Book.xlsx'
sheet_name = 'DATA'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:H',
                   header=0)


# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")

Level = st.sidebar.multiselect(
    "Select the Level:",
    options=df["Level"].unique(),
    default=df["Level"].unique()
)

User = st.sidebar.multiselect(
    "Select the User:",
    options=df["User"].unique(),
    default=df["User"].unique()
)

df_selection = df.query(
    "Level == @Level | User == @User"
)

st.dataframe(df_selection)
