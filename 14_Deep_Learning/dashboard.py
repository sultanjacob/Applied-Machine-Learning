import streamlit as st
import requests
import numpy as np

API_URL = "http://localhost:8001"

st.set_page_config(page_title="Climate Intelligence", layout="wide")
st.title("🌍 Multi-Modal Climate Intelligence")
st.write("Real-time inference dashboard connected to Dockerized FastAPI backend.")

# Sidebar Health Check
st.sidebar.header("System Diagnostics")
try:
    health_response = requests.get(f"{API_URL}/")
    if health_response.status_code == 200:
        st.sidebar.success(f"API Status: {health_response.json()['status']}")
except requests.exceptions.ConnectionError:
    st.sidebar.error("API Offline. Check Docker container.")

# Interface Tabs
tab1, tab2, tab3 = st.tabs(["Carbon Flux (Tabular)", "Deforestation (Spatial)", "Stress Forecast (Temporal)"])

with tab1:
    st.subheader("MLP: Carbon Flux Anomaly Detection")
    user_input = st.text_input("Enter 8 environmental features (comma-separated):", "0.1, 0.4, 0.5, 0.2, 0.8, 0.3, 0.9, 0.6")
    
    if st.button("Run Tabular Inference"):
        try:
            features = [float(x.strip()) for x in user_input.split(",")]
            response = requests.post(f"{API_URL}/predict/tabular", json={"features": features})
            st.json(response.json())
        except Exception as e:
            st.error(f"Error: {e}. Ensure exactly 8 numbers are provided.")

with tab2:
    st.subheader("CNN: Spatial Deforestation Detection")
    st.write("Simulating a satellite image matrix upload (64x64x3)...")
    
    if st.button("Run Spatial Inference"):
        dummy_image = np.random.rand(64, 64, 3).tolist()
        response = requests.post(f"{API_URL}/predict/spatial", json={"image_matrix": dummy_image})
        st.json(response.json())

with tab3:
    st.subheader("LSTM: Temporal Stress Forecasting")
    st.write("Simulating a 30-day weather time series (30x5)...")
    
    if st.button("Run Temporal Inference"):
        dummy_series = np.random.rand(30, 5).tolist()
        response = requests.post(f"{API_URL}/predict/temporal", json={"time_series": dummy_series})
        st.json(response.json())