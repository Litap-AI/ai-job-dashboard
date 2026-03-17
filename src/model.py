import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load data
df = pd.read_csv("output/jobs.csv")

# Create text feature
df["text"] = df["Roles Open (typical)"] + " " + df["India Locations"]

# --- STEP 1: Create labels manually ---
# 1 = relevant, 0 = not relevant
# For now we simulate preferences

def label_job(row):
    if "Data" in row["Roles Open (typical)"] or "ML" in row["Roles Open (typical)"]:
        return 1
    return 0

df["label"] = df.apply(label_job, axis=1)

# --- STEP 2: Convert text → numbers ---
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["label"]

# --- STEP 3: Train model ---
model = LogisticRegression()
model.fit(X, y)

# --- STEP 4: Predict relevance ---
df["score"] = model.predict_proba(X)[:, 1]

# --- STEP 5: Sort best jobs ---
top_jobs = df.sort_values(by="score", ascending=False)

print(top_jobs[["Company", "Roles Open (typical)", "India Locations", "score"]].head(10))
