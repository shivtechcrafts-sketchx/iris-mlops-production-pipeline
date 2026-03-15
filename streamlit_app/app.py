import streamlit as st
import requests

st.title("Iris Flower Prediction")

sepal_length = st.number_input("Sepal Length")
sepal_width = st.number_input("Sepal Width")
petal_length = st.number_input("Petal Length")
petal_width = st.number_input("Petal Width")

if st.button("Predict"):

    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=payload
    )

    st.write("Prediction:", response.json())