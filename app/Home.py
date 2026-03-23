from __future__ import annotations

import json
import os
from pathlib import Path

import streamlit as st

from app.utils.incident_loader import list_sample_incidents, load_sample_incident
from backend.triage_service import run_triage

ROOT_DIR = Path(__file__).resolve().parents[1]

st.set_page_config(page_title="AWS AI Incident Triage Assistant", layout="wide")

st.title("AWS AI Incident Triage Assistant")
st.caption("Analyze incidents, classify severity/category, and recommend runbook actions.")

with st.sidebar:
    st.header("Input Options")
    incident_files = list_sample_incidents(ROOT_DIR / "data" / "sample_incidents")
    selected_file = st.selectbox("Load sample incident", options=[""] + incident_files)
    mode = os.getenv("TRIAGE_MODE", "mock")
    st.info(f"Current triage mode: {mode}")

    if selected_file:
        loaded = load_sample_incident(ROOT_DIR / "data" / "sample_incidents" / selected_file)
        st.session_state["incident_text"] = json.dumps(loaded, indent=2)

st.subheader("Incident Input")
incident_text = st.text_area(
    "Paste an incident payload, alert details, or log snippet",
    value=st.session_state.get("incident_text", ""),
    height=300,
)

col1, col2 = st.columns([1, 2])
with col1:
    run_clicked = st.button("Run Triage", type="primary")
with col2:
    st.write("Use mock mode locally, or configure AWS credentials and Bedrock access for live model testing.")

if run_clicked:
    if not incident_text.strip():
        st.error("Please provide incident input before running triage.")
    else:
        with st.spinner("Analyzing incident..."):
            result = run_triage(incident_text=incident_text, project_root=ROOT_DIR)
            st.session_state["triage_result"] = result

if "triage_result" in st.session_state:
    result = st.session_state["triage_result"]
    st.subheader("Triage Result")
    a, b, c = st.columns(3)
    a.metric("Severity", result.get("severity", "Unknown"))
    b.metric("Category", result.get("category", "Unknown"))
    c.metric("Impacted Component", result.get("component", "Unknown"))

    st.markdown("### Summary")
    st.write(result.get("summary", "No summary available."))

    st.markdown("### Confidence")
    st.progress(min(max(float(result.get("confidence", 0.0)), 0.0), 1.0))
    st.caption(f"Confidence: {result.get('confidence', 0.0)}")

    st.markdown("### Recommended Runbook Steps")
    for step in result.get("runbook_steps", []):
        st.write(f"- {step}")
