# 🤖 Assistant: Metadata Manager — SPG Module
import streamlit as st
import pandas as pd
import openai
import json

st.set_page_config(page_title="Metadata Manager Assistant", layout="wide")
st.title("📂 Metadata Manager Assistant")
st.markdown("Automatically classify and explain metadata fields for any dataset using GPT.")

# Upload Input
uploaded_file = st.file_uploader("📤 Upload your data file (CSV format)", type=["csv"])

openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else ""

# GPT Utility Function
def generate_metadata_info(column_name):
    prompt = f"""
    You are a metadata classification engine.

    For the column name below, return a JSON object with:
    - Field Purpose
    - Suggested Metadata Tags (as a list)
    - Suggested Data Type (string, numeric, categorical, datetime, etc.)
    - Data Governance Tip (one best practice)

    Column: {column_name}

    Return ONLY valid JSON.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    try:
        return json.loads(response.choices[0].message.content.strip())
    except json.JSONDecodeError:
        return {
            "Field Purpose": "ERROR",
            "Suggested Metadata Tags": [],
            "Suggested Data Type": "ERROR",
            "Data Governance Tip": "ERROR"
        }

# Main Pipeline
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File loaded. Preview:")
    st.dataframe(df.head(), use_container_width=True)

    if st.button("🔍 Analyze Metadata Fields"):
        results = []
        for col in df.columns:
            st.info(f"🔎 Analyzing: `{col}`")
            gpt_result = generate_metadata_info(col)
            gpt_result["Column Name"] = col
            results.append(gpt_result)

        result_df = pd.DataFrame(results)
        st.success("✅ Metadata Analysis Complete")
        st.dataframe(result_df, use_container_width=True)

        # Export
        csv = result_df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Metadata Analysis CSV", csv, "metadata_analysis.csv", "text/csv")
