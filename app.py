# Streamlit app entry point
import streamlit as st
import pandas as pd
import json, time, os
from interview_flow import QUESTIONS
from evaluator import Evaluator
from llm_client import LLMClient

SAVE_TRANSCRIPTS_DIR = "transcripts"
os.makedirs(SAVE_TRANSCRIPTS_DIR, exist_ok=True)
llm = LLMClient()
eva = Evaluator()

st.set_page_config(page_title="AI Excel Mock Interviewer", layout="centered")

if "state" not in st.session_state:
    st.session_state.state = {"step": "intro", "q_idx": 0, "answers": [], "start_time": time.time()}

def show_intro():
    st.title("AI-Powered Excel Mock Interviewer — PoC")
    st.write("This PoC runs a short Excel interview (3 tasks). Upload a file when required.")
    if st.button("Start Interview"):
        st.session_state.state["step"] = "question"

def show_question(q):
    st.subheader(f"Question {st.session_state.state['q_idx']+1} / {len(QUESTIONS)}")
    st.write(q["text"])
    uploaded = None
    if q.get("file_required"):
        uploaded = st.file_uploader("Upload sheet (xlsx/csv)", type=["xlsx","xls","csv"])
    answer = st.text_area("Your answer")
    if st.button("Submit Answer"):
        file_path = None
        if uploaded is not None:
            tmp_path = f"tmp_{int(time.time())}"
            with open(tmp_path, "wb") as f: f.write(uploaded.read())
            file_path = tmp_path
        st.session_state.state["answers"].append({
            "q_idx": st.session_state.state["q_idx"], "question": q,
            "answer_text": answer, "uploaded_file": file_path
        })
        st.session_state.state["q_idx"] += 1
        if st.session_state.state["q_idx"] >= len(QUESTIONS):
            st.session_state.state["step"] = "review"
        st.experimental_rerun()

def show_review():
    st.header("Interview complete — Report")
    results = [eva.evaluate_answer(ans["question"], ans["answer_text"], ans["uploaded_file"]) for ans in st.session_state.state["answers"]]
    final = eva.aggregate_results(results)
    narrative = llm.generate_report_text(results, final)
    transcript = {"meta": {"start": st.session_state.state["start_time"], "end": time.time()}, "results": results, "final": final, "narrative": narrative}
    fname = f"{SAVE_TRANSCRIPTS_DIR}/transcript_{int(time.time())}.json"
    with open(fname, "w") as f: json.dump(transcript, f, indent=2)
    st.subheader("Score"); st.write(f"**{final['score_total']} / 100**")
    st.subheader("Breakdown"); st.json(final["breakdown"])
    st.subheader("Feedback"); st.write(narrative)

if st.session_state.state["step"] == "intro":
    show_intro()
elif st.session_state.state["step"] == "question":
    show_question(QUESTIONS[st.session_state.state["q_idx"]])
elif st.session_state.state["step"] == "review":
    show_review()
