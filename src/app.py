import streamlit as st
import pandas as pd
import os

# --- Page Config ---
st.set_page_config(page_title="AI Job Dashboard", page_icon="🚀", layout="wide")

# --- Title ---
st.title("🚀 AI Job Recommender")
st.subheader("Find the best jobs tailored to you")

st.markdown("---")

# --- Load Data (robust path handling) ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "output", "jobs.csv")

df = pd.read_csv(file_path)

# --- Clean Data ---
df.fillna("", inplace=True)

# --- Sidebar Filters ---
st.sidebar.header("🔍 Filter Options")

location = st.sidebar.selectbox(
    "Select Location",
    ["All", "Pune", "Bangalore", "Mumbai", "Delhi", "Chennai", "Remote"]
)

role = st.sidebar.selectbox(
    "Select Role",
    ["All", "Data", "ML", "SWE", "Product", "DevOps", "Risk"]
)

# --- Filtering Logic ---
filtered = df.copy()

if location != "All":
    filtered = filtered[
        filtered["India Locations"].str.contains(location, case=False, na=False)
    ]

if role != "All":
    filtered = filtered[
        filtered["Roles Open (typical)"].str.contains(role, case=False, na=False)
    ]

# --- Show Filtered Jobs ---
st.markdown("## 📋 Filtered Jobs")

st.write(f"Total jobs found: **{len(filtered)}**")

# --- Make links clickable ---
filtered["Application Link"] = filtered["Application Link"].apply(
    lambda x: f"[Apply Here]({x})"
)

st.markdown(filtered.to_markdown(index=False), unsafe_allow_html=True)

st.markdown("---")

# --- Ranking (simple relevance scoring) ---
def calculate_score(row):
    score = 0

    if location != "All" and location.lower() in row["India Locations"].lower():
        score += 1

    if role != "All" and role.lower() in row["Roles Open (typical)"].lower():
        score += 1

    return score


if len(filtered) > 0:
    filtered["score"] = filtered.apply(calculate_score, axis=1)
    top_jobs = filtered.sort_values(by="score", ascending=False)

    # --- Top Recommendation ---
    st.markdown("## 🔥 Top Recommendation")

    top_job = top_jobs.iloc[0]

    st.success(f"""
    **{top_job['Company']}**
    
    📌 Role: {top_job['Roles Open (typical)']}  
    📍 Location: {top_job['India Locations']}  
    🔗 [Apply Here]({top_job['Application Link'].split('(')[-1][:-1]})
    """)

    st.markdown("---")

    # --- Ranked Jobs Table ---
    st.markdown("## 📊 Ranked Jobs")

    st.dataframe(top_jobs.reset_index(drop=True))

else:
    st.warning("No jobs found for selected filters.")
