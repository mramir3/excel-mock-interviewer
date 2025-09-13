<<<<<<< HEAD
# AI-Powered Excel Mock Interviewer

## Overview
This is a Proof-of-Concept (PoC) system that simulates an Excel technical interview.  
It conducts a structured interview, evaluates answers, manages state, and generates a feedback report.

## Features
- Multi-turn Excel Q&A interview flow
- Deterministic evaluation (pandas-based)
- LLM-powered narrative feedback
- Session transcript saving
- Streamlit front-end

## Run Locally
```bash
pip install -r requirements.txt
export OPENAI_API_KEY="your_key"
streamlit run app.py
```

## Deployment
- Easiest: Deploy directly to [Streamlit Cloud](https://streamlit.io/cloud).

## Repo Structure
- `app.py` — Streamlit front-end + state machine
- `interview_flow.py` — interview questions & config
- `evaluator.py` — deterministic checks
- `llm_client.py` — wrapper for LLM-based feedback
- `sample_data/` — example Excel/CSV files
- `transcripts/` — auto-saved interview sessions

## Deliverables
- PoC code (this repo)
- Deployed app link (Streamlit Cloud recommended)
- Sample transcripts in `/transcripts`
=======
# excel-mock-interviewer
>>>>>>> 6b2df1a0030e9944f26fedd4ceedb395f266625f
