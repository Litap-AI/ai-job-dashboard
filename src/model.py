import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# --- Basic Rule-Based Ranking (fallback) ---
def calculate_score(row, location, role):
    score = 0

    if location != "All" and location.lower() in row["India Locations"].lower():
        score += 1

    if role != "All" and role.lower() in row["Roles Open (typical)"].lower():
        score += 1

    return score


def rank_jobs(df, location, role):
    ranked_df = df.copy()

    ranked_df["score"] = ranked_df.apply(
        lambda row: calculate_score(row, location, role),
        axis=1
    )

    ranked_df = ranked_df.sort_values(by="score", ascending=False)

    return ranked_df


# --- NLP Resume-Based Ranking ---
def rank_jobs_with_resume(df, resume_text):
    df = df.copy()

    # Combine job text fields
    df["job_text"] = (
        df["Roles Open (typical)"].fillna("") + " " +
        df["India Locations"].fillna("")
    )

    # Initialize TF-IDF
    vectorizer = TfidfVectorizer(stop_words="english")

    # Fit on resume + jobs
    vectors = vectorizer.fit_transform([resume_text] + df["job_text"].tolist())

    resume_vector = vectors[0]
    job_vectors = vectors[1:]

    # Compute similarity
    similarity_scores = cosine_similarity(resume_vector, job_vectors)[0]

    df["score"] = similarity_scores

    # Sort by similarity
    df = df.sort_values(by="score", ascending=False)

    return df
