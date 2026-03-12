import streamlit as st
from database import login

st.title("🔐 Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):

    user = login(username,password)

    if user:
        st.success("Login Successful")
        st.session_state["user"] = username
        st.session_state["role"] = user[3]
    else:
        st.error("Invalid Credentials")