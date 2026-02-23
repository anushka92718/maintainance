import streamlit as st

st.title("Simple input app")
name = st.text_input("Enter your name")
if st.button("Submit"):
    st.write("Hello", name)