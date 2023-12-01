
# example/st_app_gsheets_using_service_account.py

import pandas as pd
import plotly.express as px
from PIL import Image
import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title='Tank Monitor Feed')
# Center-align the title using HTML
st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Custom CSS to center-align the DataFrame
st.markdown("""
    <style>
    .dataframe {
        display: block;
        margin-left: auto;
        margin-right: auto;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Display the centered title
st.markdown("<h1 class='centered-title'>Tank Monitor Feed</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='centered-title'>- Developed by Spectramat Engineering Team</h4>", unsafe_allow_html=True)

#Establishing the connection with the datasheet
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

#Reading of Data
df_NickelStrike = conn.read(worksheet="NiStrike", usecols=list(range(5)), ttl=5)
df_AuStrike = conn.read(worksheet="AuStrike", usecols=list(range(5)), ttl=5)
df_NickelPlate = conn.read(worksheet="NiPlate", usecols=list(range(5)), ttl=5)
df_AuPlate = conn.read(worksheet="AuPlate", usecols=list(range(5)), ttl=5)

# Streamlit selection for department
department = ['Nickel Strike', 'Au Strike', 'Nickel Plate', 'Au Plate']
department_selection = st.multiselect('Department:', department, default=department)

# Display selected DataFrame(s)
if 'Nickel Strike' in department_selection:
    st.markdown("<h4 class='centered-title'>- Nickel Strike Data </h4>", unsafe_allow_html=True)
    st.dataframe(df_NickelStrike)

if 'Au Strike' in department_selection:
    st.markdown("<h4 class='centered-title'>- Au Strike Data </h4>", unsafe_allow_html=True)
    st.dataframe(df_AuStrike)

if 'Nickel Plate' in department_selection:
    st.markdown("<h4 class='centered-title'>- Nickel Plate Data </h4>", unsafe_allow_html=True)
    st.dataframe(df_NickelPlate)

if 'Au Plate' in department_selection:
    st.markdown("<h4 class='centered-title'>- AU Plate Data </h4>", unsafe_allow_html=True)
    st.dataframe(df_AuPlate)