import streamlit as st
import joblib
import pandas as pd

model = joblib.load('model.pkl')

st.title("Insurance Price Estimator")
st.write("Trained on real world data(US), it has 57% accuracy and can predict the insurance price .")

age = st.number_input("Enter your age", min_value=18, max_value=100, value=30, step=1)
sex = st.selectbox("Select your gender", ["Male", "Female"])
bmi = st.number_input("Enter your BMI", min_value=10.0, max_value=50.0, value=25.0, step=0.1)
children = st.selectbox("Number of children", [0, 1, 2, 3, 4])
smoker = st.radio("Are you a smoker?", ["Yes", "No"])
region = st.selectbox("Select your region", ["Northeast", "Northwest", "Southeast", "Southwest"])

def predict_insurance_price(age, sex, bmi, children, smoker, region):
    features = pd.DataFrame([{'age': age,
                               'sex': sex,
                               'bmi': bmi,
                               'children': children,
                               'smoker': smoker,
                               'region': region}])
    prediction = model.predict(features)
    return prediction[0]

if st.button("Tell me the insurance price"):
    price = predict_insurance_price(age, sex, bmi, children, smoker, region)
    st.text(f"The estimated insurance price is: ${price:.2f}")