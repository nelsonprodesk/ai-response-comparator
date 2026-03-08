import streamlit as st
from difflib import Differ

st.title("AI Response Comparator")

response1 = st.text_area("Model 1 Response")
response2 = st.text_area("Model 2 Response")

if st.button("Compare Responses"):
    r1 = response1.split()
    r2 = response2.split()

    d = Differ()
    result = list(d.compare(r1, r2))

    st.subheader("Comparison Result")
    st.text("\n".join(result))
