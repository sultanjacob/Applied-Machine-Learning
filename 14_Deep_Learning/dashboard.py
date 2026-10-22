import streamlit as st
import requests
import numpy as np
import pandas as pd
from PIL import Image

API_URL = "http://localhost:8001"

st.set_page_config(page_title="Climate Intelligence", layout="wide")
st.title("🌍 Multi-Modal Climate Intelligence")

# Sidebar Health Check
st.sidebar.header("System Diagnostics")
try:
    health = requests.get(f"{API_URL}/")
    st.sidebar.success(f"API Status: {health.json()['status']}") if health.status_code == 200 else st.sidebar.error("API Error")
except requests.exceptions.ConnectionError:
    st.sidebar.error("API Offline. Check Docker container.")

tab1, tab2, tab3 = st.tabs(["Carbon Flux", "Deforestation", "Stress Forecast"])

with tab1:
    st.subheader("MLP: Carbon Flux Anomaly Detection")
    user_input = st.text_input("Enter 8 environmental features (comma-separated):", "0.1, 0.4, 0.5, 0.2, 0.8, 0.3, 0.9, 0.6")
    if st.button("Run Tabular Inference"):
        features = [float(x.strip()) for x in user_input.split(",")]
        res = requests.post(f"{API_URL}/predict/tabular", json={"features": features})
        st.json(res.json()) if res.status_code == 200 else st.error(res.text)

with tab2:
    st.subheader("CNN: Spatial Deforestation Detection")
    uploaded_img = st.file_uploader("Upload Satellite Image (JPG/PNG)", type=["jpg", "png", "jpeg"])
    if uploaded_img and st.button("Run Spatial Inference"):
        image = Image.open(uploaded_img).resize((64, 64)).convert('RGB')
        img_array = np.array(image) / 255.0
        res = requests.post(f"{API_URL}/predict/spatial", json={"image_matrix": img_array.tolist()})
        st.json(res.json()) if res.status_code == 200 else st.error(res.text)

with tab3:
    st.subheader("LSTM: Temporal Stress Forecasting")
    uploaded_csv = st.file_uploader("Upload 7-Day Weather Data (CSV, 3 numerical columns)", type=["csv"])
    if uploaded_csv and st.button("Run Temporal Inference"):
        df = pd.read_csv(uploaded_csv)
        if df.shape == (7, 3):
            res = requests.post(f"{API_URL}/predict/temporal", json={"time_series": df.values.tolist()})
            st.json(res.json()) if res.status_code == 200 else st.error(res.text)
        else:
            st.error(f"CSV must be exactly 7 rows and 3 columns. Detected shape: {df.shape}")
