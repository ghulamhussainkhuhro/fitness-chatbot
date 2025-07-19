# app.py

import streamlit as st
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from chatbot.chain import build_chain
from chatbot.utils import is_safe_query

st.set_page_config(page_title="Fitness Coach AI Assistant", page_icon="💪")

st.title("💪 Ask the Fitness Coach Bot!")
st.write("Ask me anything about training programs, pricing, and how online fitness coaching works.")

chain = build_chain()

user_input = st.text_input("Enter your question:")

if user_input:
    if not is_safe_query(user_input):
        st.warning("⚠️ Sorry, I cannot provide advice on supplements or health. Please consult a professional.")
    else:
        with st.spinner("Thinking..."):
            response = chain.invoke({"question": user_input})
            st.success("Answer:")
            st.write(response)
