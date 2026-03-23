from pathlib import Path
import json

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parents[2]
runbooks_path = ROOT_DIR / "data" / "runbooks" / "runbooks.json"

st.title("Runbook Library")
runbooks = json.loads(runbooks_path.read_text(encoding="utf-8"))
for category, steps in runbooks.items():
    st.subheader(category)
    for step in steps:
        st.write(f"- {step}")
