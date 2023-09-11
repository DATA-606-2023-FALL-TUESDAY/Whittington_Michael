# imports
import streamlit as st
import pandas as pd
import plotly.express as px
from ydata_quality import DataQuality

# Read the Excel file
@st.cache
def load_data(file):
    return pd.read_excel(file)

# Streamlit app
def main():
    st.title("Excel Spreadsheet Explorer")

    uploaded_file = st.file_uploader("Upload your Excel file", type=['xlsx'])

    if uploaded_file:
        df = load_data(uploaded_file)
        st.write(df.head())

        # Data Profiling using ydata-quality
        data_quality = DataQuality(df)
        quality_results = data_quality.evaluate()
        st.write("Data Quality Report:")
        st.json(quality_results['warnings'])

        # Data Visualization
        col_list = df.columns.tolist()
        x_axis = st.selectbox("Select X axis:", col_list)
        y_axis = st.selectbox("Select Y axis:", col_list)

        plot = px.scatter(df, x=x_axis, y=y_axis)
        st.plotly_chart(plot)

if __name__ == "__main__":
    main()
