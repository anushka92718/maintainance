import streamlit as st
st.title("Simple Chatbot")

Question = st.text_input("Ask me anything")

if st.button("send"):
    st.write("You asked : ", Question)
    st.write("Chatbot is on the process, I will reply soon")