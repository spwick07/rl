import streamlit as st
import requests

st.title("🧠 Expiry Strategy Predictor")

units = st.slider("Units Left", 1, 100)
days = st.slider("Days to Expiry", 1, 10)
cost = st.number_input("Per Unit Cost", min_value=1.0, value=10.0)
total = units * cost

if st.button("Suggest Strategy"):
    data = {"units_left": units, "days_to_expiry": days, "per_unit_cost": cost, "total_cost": total}
    res = requests.post("http://localhost:8000/predict-strategy/", json=data)
    st.success(f"Suggested Strategy: {res.json()['strategy']}")
