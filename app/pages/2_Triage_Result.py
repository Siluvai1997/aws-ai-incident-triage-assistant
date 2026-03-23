import streamlit as st

st.title("Triage Result")
result = st.session_state.get("triage_result")
if not result:
    st.info("Run triage from the Home page to view results here.")
else:
    st.json(result)
