import streamlit as st
import pandas as pd
from src.analyzer import find_groups
from src.explainer import explain_group
from src.recommender import recommend

st.title("AI Learning Equity Assistant")

uploaded = st.file_uploader("Upload a CSV with student data")

if uploaded:
    df = pd.read_csv(uploaded)
    df = find_groups(df)

    st.subheader("Detected Groups")
    st.dataframe(df)

    group_id = st.selectbox("Select a Group", df["group"].unique())

    st.subheader("Explanation")
    st.write(explain_group(df, group_id))

    st.subheader("Recommendations")
    recs = recommend(df, group_id)
    for r in recs:
        st.write("•", r)
