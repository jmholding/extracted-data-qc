import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Upload a Raw Structured Data (RSD) Excel file")
if uploaded_file is not None:
    if ".xlsx" in uploaded_file.name:
        xlsx = pd.ExcelFile(uploaded_file)
        dfs = []
        try:
            for sheet in xlsx.sheet_names:
                dfs.append(pd.read_excel(xlsx, sheet))
        except:
            st.write("Could not parse file contents")
        
        if len(dfs) > 0:
            for df in dfs:
                st.write(df)
                
    else:
        "Invalid file - please try again"
