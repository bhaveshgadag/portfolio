import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Bhavesh Gadag")
    content = """
    Hi, I am Bhavesh, I'm a Python Programmer and currently I'm trying to improve my Python skills through Python Mega Course.
    """
    st.info(content)

content = """
Below you can find some of the apps which I have built in Python.
"""
st.write()
