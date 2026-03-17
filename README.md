# AI Job Dashboard 🚀

## 📌 Project Overview
This project extracts job listings from a PDF and builds a system to filter and analyze relevant jobs.

Goal: Automate job discovery and filtering using Python and later ML.

---

## ⚙️ Features (Current)

### ✅ 1. PDF Data Extraction
- Extracts structured job data from raw PDF
- Converts into usable dataset (CSV)

### ✅ 2. Data Cleaning
- Removes noisy columns
- Standardizes job data

### ✅ 3. Job Filtering System
- Filter by location (e.g., Pune, Bengaluru)
- Filter by role (e.g., Data, SWE)
- Combined filtering

---

## 📊 Example Use Case

Filter:
- Location: Pune
- Role: Data

Output:
- American Express
- Siemens India

---

## 🛠️ Tech Stack
- Python
- Pandas
- Tabula (PDF extraction)

---

## 📂 Project Structure
## 🤖 ML Job Ranking

The system uses TF-IDF + Logistic Regression to rank jobs based on relevance.

### Example Output:

| Company | Role | Location | Score |
|--------|------|---------|------|
| Procter & Gamble | Ops, Data | Mumbai | 0.88 |
| Barclays | SWE, Data | Bengaluru | 0.85 |

Higher score = more relevant job
