import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Bhavesh Gadag")
    content = """
    Hi, I am Bhavesh, I'm a Python Programmer and currently I'm learning to improve my Python skills through Python Mega Course.
    I graduated in 2019 in Bachelor of Science in Computer Science from the University of Mumbai. 
    I have worked as a Intern Programmer at Rock Solid Solutions   
    """
    st.info(content)

content = """
Below you can find some of the apps which I have built in Python.
"""
st.write(content)

data = pandas.read_csv("data.csv", delimiter=";")
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in data[:9].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in data[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
