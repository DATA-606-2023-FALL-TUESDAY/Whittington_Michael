import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Load the NEISS dataset
@st.cache
def load_data():
    return pd.read_csv('neiss_2022.csv')

data = load_data()

# App title
st.title('NEISS Data Exploration')

# Display a subset of the data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# Data Profiling with pandas_profiling
if st.sidebar.checkbox('Generate data profiling report'):
    st.subheader('Data Profiling Report')
    report = ProfileReport(data, explorative=True)
    st_profile_report(report)
