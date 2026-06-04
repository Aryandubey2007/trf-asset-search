import streamlit as st
import pandas as pd

st.set_page_config(page_title="TRF Asset Search", layout="wide")

st.title("TRF LTD Asset Search System")
st.write("Enter user name to find assigned asset details.")

file_name = "Asset Data Base 30.03.2026 TRF LTD.xlsx"
sheet = "IN Use & IT Stock"

try:
    df = pd.read_excel(file_name, sheet_name=sheet)

    name = st.text_input("Enter user name or employee ID")

    cols = [
        "User",
        "Asset Tag",
        "Asset Type",
        "Acquisition Date",
        "Category",
        "Designation",
        "Employee ID",
        "Email",
        "Mobile",
        "Department",
        "SAP CODE",
        "Asset State",
        "Product Type",
        "Serial Number",
        "Product Make/Model",
        "Processor Name/Speed"
    ]

    if st.button("Search"):
        if name.strip() == "":
            st.warning("Please enter a user name.")
        else:
            result = df[
                df["User"].astype(str).str.contains(name, case=False, na=False) |
                df["Employee ID"].astype(str).str.contains(name, case=False, na=False)
                ]
            if result.empty:
                st.error("User not found")
            else:
                st.success(f"{len(result)} record(s) found for: {name}")
                st.dataframe(result[cols], use_container_width=True)

except FileNotFoundError:
    st.error("Excel file not found. Keep Excel file and app.py in the same folder.")

except ValueError:
    st.error("Sheet name not found. Check the Excel sheet name.")


st.write("App loaded successfully")