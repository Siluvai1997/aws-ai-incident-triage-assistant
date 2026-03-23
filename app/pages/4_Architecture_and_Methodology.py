import streamlit as st

st.title("Architecture and Methodology")
st.markdown(
    """
This MVP demonstrates an AI-assisted operational triage workflow.

**Flow**
1. Streamlit frontend accepts incident input
2. Backend triage service prepares a structured prompt
3. Amazon Bedrock returns summary, severity, category, component, and confidence
4. Runbook mapping adds recommended action steps
5. Results are presented in the UI

**Design choices**
- Serverless backend for low cost and event-driven execution
- Bedrock for managed generative AI inference
- Terraform for repeatable infrastructure setup
- CloudWatch for logs and troubleshooting
- Local-first frontend to avoid always-on cloud spend
"""
)
