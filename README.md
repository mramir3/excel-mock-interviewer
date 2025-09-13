# 📊 AI-Powered Excel Mock Interviewer

An AI-powered system that simulates **Excel-based technical interviews**, evaluates answers intelligently, and generates structured feedback reports.

---

## 🚀 Live Demo

👉 [Streamlit App – Excel Mock Interviewer](https://excel-mock-interviewer-kk6cgqy47cbeqbq2gngbnw.streamlit.app/)

---

## 📂 Repository Structure

```
excel-mock-interviewer/
│
├── app.py               # Streamlit UI for conducting interviews
├── evaluator.py         # Evaluates answers (rule-based + LLM-based)
├── interview_flow.py    # Handles interview questions & flow logic
├── llm_client.py        # LLM API client for intelligent evaluation
├── requirements.txt     # Dependencies
├── transcripts/         # Stores interview session logs in JSON
└── README.md            # Project documentation
```

---

## ⚙️ Features

* ✅ Structured interview flow (Excel/analytics questions)
* ✅ Dual evaluation strategy: deterministic + LLM-based
* ✅ Transcript logging for every session (`/transcripts/`)
* ✅ Automated feedback report with scores & insights
* ✅ Deployed and accessible via Streamlit Cloud

---

## 🛠 Tech Stack

* **Language:** Python 3.12
* **Frontend & Deployment:** Streamlit Cloud
* **Libraries:**

  * `streamlit` – interactive UI
  * `openai` / `transformers` – for LLM-based evaluation
  * `json` – transcript storage
  * `random` – sampling questions

---

## 📑 Sample Transcript

Example saved in `/transcripts/transcript_2025-09-12_21-45.json`:

```json
{
  "q": "Write a formula to calculate the average of cells A1 to A10.",
  "a": "=SUM(A1:A10)",
  "evaluation": "Incorrect. Candidate confused SUM with AVERAGE. Correct formula is =AVERAGE(A1:A10).",
  "score": 2
}
```

---

## 🏗 How to Run Locally

1. Clone the repo:

   ```bash
   git clone https://github.com/mramir3/excel-mock-interviewer.git
   cd excel-mock-interviewer
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # (Linux/Mac)
   venv\Scripts\activate      # (Windows)
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

---

## 👤 Author

**Amir Ansary**

* 📧 [ansaryamir7@gmail.com](mailto:ansaryamir7@gmail.com)
* 🌐 [LinkedIn](https://www.linkedin.com/in/mramir11)
* 💻 [GitHub](https://github.com/mramir3)

---
