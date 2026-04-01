import streamlit as st
import pickle
import numpy as np

# Load model & scaler
model = pickle.load(open("logistic_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("Customer Churn Prediction")

# Example inputs (change based on your dataset)
tenure = st.number_input("Tenure")
balance = st.number_input("Balance")
num_products = st.number_input("Number of Products")

if st.button("Predict"):
    input_data = np.array([tenure, balance, num_products])
    input_scaled = scaler.transform([input_data])

    prediction = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][1]

    if prediction == 1:
        st.error(f"Customer likely to churn (Probability: {prob:.2f})")
    else:
        st.success(f"Customer will stay (Probability: {prob:.2f})")