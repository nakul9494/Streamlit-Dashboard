import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="💡 Crazy Cool Dashboard", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #1e1e2f;
            color: #f0f0f0;
        }
        .block-container {
            padding-top: 2rem;
        }
        .stSelectbox label, .stTextInput label {
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🚀 Navigation")
st.sidebar.markdown("Upload your file, filter the data, and explore visualizations!")

uploaded_file = st.sidebar.file_uploader("📂 Choose a CSV file", type="csv")

# Title and Subtitle
st.title("🎯 Simple Data Dashboard")
st.caption("A fun and interactive way to explore your data!")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Data Preview
    st.subheader("👀 Data Preview")
    st.dataframe(df.head(), use_container_width=True)

    # Data Summary
    st.subheader("📊 Data Summary")
    st.dataframe(df.describe(), use_container_width=True)

    # Filter Section
    st.subheader("🔎 Filter Data")
    with st.expander("Customize Filter"):
        columns = df.columns.tolist()
        selected_column = st.selectbox("🎯 Select column to filter by", columns)
        unique_values = df[selected_column].unique()
        selected_value = st.selectbox("🎯 Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.success(f"Filtered {len(filtered_df)} rows where `{selected_column}` is `{selected_value}`")
    st.dataframe(filtered_df, use_container_width=True)

    # Plot Section
    st.subheader("📈 Plot Data")
    col1, col2 = st.columns(2)
    with col1:
        x_column = st.selectbox("🧭 Select x-axis", columns)
    with col2:
        y_column = st.selectbox("🧭 Select y-axis", columns)

    if st.button("✨ Generate Plot"):
        st.markdown(f"### 📌 Plot of `{y_column}` vs `{x_column}`")
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.warning("👈 Upload a CSV file from the sidebar to get started!")
