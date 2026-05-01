import streamlit as st
import pandas as pd
from utils.causal import run_causal_analysis
from utils.visualize import plot_distribution

st.set_page_config(page_title="AI Causal Inference Engine", layout="wide")

st.title("🧠 AI Causal Inference Engine")

st.write("Discover cause-effect relationships, not just correlations.")

file = st.file_uploader("Upload Dataset (CSV)", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

    columns = df.columns.tolist()

    cause = st.selectbox("Select Cause Variable", columns)
    effect = st.selectbox("Select Effect Variable", columns)

    if st.button("Run Causal Analysis"):
        result = run_causal_analysis(df, cause, effect)

        st.subheader("📊 Causal Effect Result")
        st.success(result["summary"])

        st.write("### 📌 Detailed Output")
        st.write(result["details"])

        st.write("### 📈 Data Distribution")
        plot_distribution(df, cause, effect)
