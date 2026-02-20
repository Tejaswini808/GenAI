import streamlit as st
import numpy as np
import pandas as pd

st.title("My Streamlit App")
st.write("This is a simple Streamlit app.")
st.text("You can add more features and functionality as needed.")

name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write(f"Hello, {name}! Welcome to Streamlit.")

#Display a random dataframe as a line chart and bar chart
df = pd.DataFrame(np.random.rand(10, 2), columns=['Column 1', 'Column 2'])
st.line_chart(df)
st.bar_chart(df)

#Media layout and advanced widgets
st.sidebar.title("Navigation")
st.image("E:\genai\scikit.png", caption="Sample Image")
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

#file uploading and caching topics

upload_file = st.file_uploader("Upload a CSV file", type=["csv"])
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

st.title("Text and Markdown Demo")
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("This is **bold** text, this is *italic* text, and this is a [link](https://www.streamlit.io).")
st.code("print('Hello, Streamlit!')", language="python")
st.text_input("What's your name???")
st.text_area("Write something about yourself:")
st.number_input("Pick the number", min_value=0, max_value=100)
st.slider("Choose a range", 0, 100, (25, 75))
st.selectbox("Select a fruit", ["Apple", "Banana", "Orange"])
st.multiselect("Select your favorite colors", ["Red", "Green", "Blue", "Yellow"])
st.radio("Pick one",["Option A","Option B"])
st.checkbox("I agree to the terms and conditions")

option = st.radio("choose view",["show chart","show table"])
if option == "show chart":
    st.write("Displaying chart...")
else:
    st.write("Displaying table...")


with st.form("login_form"):
    st.write("Please log in")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")
   
    if submitted:
        st.write(f"Welcome, {username}!")