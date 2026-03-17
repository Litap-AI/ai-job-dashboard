import streamlit as st
import pandas as pd
import os

from filter import filter_jobs
from model import rank_jobs

# --- Page Config ---
st.set_page_config(page_title="AI Job Dashboard", page_icon="🚀", layout="wide")

# --- Title ---
st.title("🚀 AI Job Recommender")
st.subheader("Find the best jobs tailored to you")

st.markdown("---")

# --- Load Data ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "output", "jobs.csv")

df = pd.read_csv(file_path)
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

# --- Apply Filtering ---
filtered = filter_jobs(df, location, role)

st.markdown("## 📋 Filtered Jobs")
st.write(f"Total jobs found: **{len(filtered)}**")

# --- Clickable Links ---
def make_clickable(link):
    return f"[Apply Here]({link})"

if len(filtered) > 0:
    filtered_display = filtered.copy()
    filtered_display["Application Link"] = filtered_display["Application Link"].apply(make_clickable)

    st.markdown(filtered_display.to_markdown(index=False), unsafe_allow_html=True)

    st.markdown("---")

    # --- Ranking ---
    top_jobs = rank_jobs(filtered, location, role)

    # --- Top Recommendation ---
    st.markdown("## 🔥 Top Recommendation")

    top_job = top_jobs.iloc[0]

    st.success(f"""
    **{top_job['Company']}**

    📌 Role: {top_job['Roles Open (typical)']}  
    📍 Location: {top_job['India Locations']}  
    🔗 [Apply Here]({top_job['Application Link']})
    """)

    st.markdown("---")

    # --- Ranked Table ---
    st.markdown("## 📊 Ranked Jobs")
    st.dataframe(top_jobs.reset_index(drop=True))

else:
    st.warning("No jobs found for selected filters.")
