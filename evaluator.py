import pandas as pd, re

class Evaluator:
    def evaluate_answer(self, question, answer_text, uploaded_file):
        res = {"qid": question["id"], "score": 0, "notes": []}
        gt = question["ground_truth"]
        if gt["action"] == "sum":
            if uploaded_file: df = self._load(uploaded_file); total = df[gt["column"]].sum(); res["computed"] = total
        if "SUM" in answer_text.upper(): res["score"] += 40; res["notes"].append("Used SUM formula")
        return res

    def aggregate_results(self, results):
        total = sum(r["score"] for r in results)
        return {"score_total": total, "breakdown": {r["qid"]: r for r in results}}

    def _load(self, path):
        if path.endswith(".csv"): return pd.read_csv(path)
        return pd.read_excel(path)
