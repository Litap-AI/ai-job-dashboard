import streamlit as st
import pandas as pd
import PyPDF2

from filter import filter_jobs
from model import rank_jobs, rank_jobs_with_resume
# --- Page Config ---
st.set_page_config(page_title="AI Job Recommender", layout="wide")

# --- Load Data ---
@st.cache_data
def load_data():
    return pd.read_csv("output/jobs.csv")

df = load_data()

# --- Title ---
st.title("🚀 AI Job Recommender")
st.write("Find the best jobs tailored to you")

# --- Sidebar Filters ---
st.sidebar.header("🔎 Filter Options")

def extract_unique_locations(df):
    locations = set()

    for loc in df["India Locations"].dropna():
        parts = loc.split(",")
        for p in parts:
            clean = p.strip().split("(")[0].strip()
            locations.add(clean)

    return sorted(locations)


unique_locations = extract_unique_locations(df)

location = st.sidebar.selectbox(
    "Select Location",
    ["All"] + unique_locations
)

role = st.sidebar.selectbox(
    "Select Role",
    ["All", "Data", "ML", "SWE", "AI"]
)

# --- Resume Upload ---
st.subheader("📄 Upload Resume (PDF)")
uploaded_file = st.file_uploader("Upload your resume", type=["pdf"])

# --- Resume Text Extraction ---
def extract_resume_text(uploaded_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    for page in pdf_reader.pages:
        content = page.extract_text()
        if content:
            text += content

    return text

# --- Process Data ---
if uploaded_file is not None:
    st.success("Resume uploaded successfully ✅")

    resume_text = extract_resume_text(uploaded_file)

    ranked_df = rank_jobs_with_resume(df, resume_text)

else:
    filtered_df = filter_jobs(df, location, role)
    ranked_df = rank_jobs(filtered_df, location, role)

# --- Filtered Jobs ---
st.subheader("📋 Filtered Jobs")

if uploaded_file is None:
    st.write(f"Total jobs found: {len(filtered_df)}")
    st.dataframe(filtered_df.head(10))
else:
    st.write("Showing jobs ranked based on your resume")

# --- Ranked Jobs ---
st.subheader("🔥 Ranked Jobs")

st.dataframe(ranked_df.head(10))

# --- Top Recommendation ---
st.subheader("🌟 Top Recommendation")

top_job = ranked_df.iloc[0]

st.success(f"🏢 {top_job['Company']}")

st.write(f"📌 Role: {top_job['Roles Open (typical)']}")
st.write(f"📍 Location: {top_job['India Locations']}")

if "Application Link" in top_job:
    st.markdown(f"[🔗 Apply Here](https://{top_job['Application Link']})")

st.write(f"⭐ Score: {round(top_job['score'], 3)}")
