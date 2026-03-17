# 🚀 AI Job Recommender System

A smart job recommendation system that filters and ranks jobs based on user preferences and resume content using NLP techniques.

---

## 📌 Overview

This project is designed to help users find relevant job opportunities efficiently.

It supports:

* 🔍 Filtering jobs by location and role
* 📄 Resume-based job recommendations using NLP
* 📊 Ranking jobs based on similarity scores

The system combines rule-based filtering with machine learning techniques to provide personalized job suggestions.

---

## 🧠 How It Works

### 1. Without Resume

* User selects location and role
* Jobs are filtered using keyword matching
* Jobs are ranked using a simple scoring system

### 2. With Resume (NLP-based)

* Resume is uploaded as a PDF
* Text is extracted using PyPDF2
* TF-IDF vectorization converts text into numerical form
* Cosine similarity compares resume with job descriptions
* Jobs are ranked based on similarity scores

---

## ⚙️ Features

* 📍 Clean location filtering (unique city extraction)
* 🎯 Role-based filtering
* 📄 Resume upload support (PDF)
* 🤖 NLP-based recommendation system
* 📊 Ranked job results with scores
* 🌟 Top job recommendation highlight
* 💻 Interactive UI using Streamlit

---

## 🧰 Tech Stack

* **Python**
* **Pandas**
* **Scikit-learn**
* **Streamlit**
* **PyPDF2**

---

## 📂 Project Structure

```
ai-job-dashboard/
│
├── output/
│   └── jobs.csv
│
├── src/
│   ├── app.py        # Streamlit UI
│   ├── filter.py     # Filtering logic
│   └── model.py      # Ranking + NLP logic
│
├── assets/           # Screenshots
│   ├── ui.png
│   ├── resume.png
│   └── recommendation.png
│
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone https://github.com/litap-AI/ai-job-dashboard.git
cd ai-job-dashboard
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the app

```
streamlit run src/app.py
```

---

## 📸 Screenshots

### 🔹 UI Interface

![UI](assets/ui.png)

### 🔹 Resume Upload & Ranking

![Resume](assets/resume.png)

### 🔹 Top Recommendation

![Recommendation](assets/recommendation.png)

---

## 🚀 Future Improvements

* 🔎 Skill extraction from resume
* 🧠 Advanced NLP using BERT embeddings
* 🌐 Deployment on Streamlit Cloud
* 📊 Better ranking using weighted scoring
* 📍 Remote job filtering

---

## 🎯 Key Learnings

* Building end-to-end ML applications
* Data preprocessing and cleaning
* NLP techniques (TF-IDF, cosine similarity)
* Streamlit for rapid UI development
* Modular code structure

---

## 📬 Contact

If you found this project useful or have suggestions, feel free to connect.

---

## ⭐ Acknowledgment

This project was built as part of a hands-on learning journey in AI/ML and real-world application development.
