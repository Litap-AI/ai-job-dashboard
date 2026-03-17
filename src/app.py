import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("output/jobs.csv")

# Title
st.title("AI Job Dashboard 🚀")

# User inputs
location = st.text_input("Enter Location (e.g., Pune, Bengaluru)")
role = st.text_input("Enter Role (e.g., Data, ML, SWE)")

# Filter button
if st.button("Find Jobs"):

    filtered = df.copy()

    if location:
        filtered = filtered[
            filtered["India Locations"].str.contains(location, case=False, na=False)
        ]

    if role:
        filtered = filtered[
            filtered["Roles Open (typical)"].str.contains(role, case=False, na=False)
        ]

    st.subheader("Filtered Jobs")
    st.write(filtered)

    # Simple ranking (reuse logic)
    filtered["score"] = filtered["Roles Open (typical)"].apply(
        lambda x: 1 if "Data" in x or "ML" in x else 0
    )

    ranked = filtered.sort_values(by="score", ascending=False)

    st.subheader("Ranked Jobs")
    st.write(ranked)
