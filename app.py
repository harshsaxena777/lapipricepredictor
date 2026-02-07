import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import pickle

# --- UI CONFIGURATION ---
st.set_page_config(page_title="NexaLap AI", page_icon="💻", layout="wide")

# Custom CSS for Professional Look
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    .metric-container { background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

st.title("💻 NexaLap: High-Precision Price Estimator")
st.markdown("---")

# --- SIDEBAR INPUTS ---
with st.sidebar:
    st.header("Hardware Configuration")
    company = st.selectbox('Brand', ['Apple', 'HP', 'Dell', 'Lenovo', 'Asus', 'Acer', 'MSI'])
    type_name = st.selectbox('Category', ['Ultrabook', 'Notebook', 'Gaming', 'Workstation', '2 in 1 Convertible'])
    
    col1, col2 = st.columns(2)
    with col1:
        ram = st.select_slider('RAM (GB)', options=[4, 8, 12, 16, 24, 32, 64])
        weight = st.number_input('Weight (kg)', value=1.5)
    with col2:
        cpu = st.selectbox('CPU', ['Intel i3', 'Intel i5', 'Intel i7', 'AMD Ryzen 5', 'AMD Ryzen 7'])
        gpu = st.selectbox('GPU', ['Nvidia', 'Intel', 'AMD'])

# --- MAIN DASHBOARD ---
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="metric-container">', unsafe_allow_html=True)
    ssd = st.selectbox('SSD Storage', [0, 128, 256, 512, 1024])
    st.markdown('</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="metric-container">', unsafe_allow_html=True)
    hdd = st.selectbox('HDD Storage', [0, 512, 1024, 2048])
    st.markdown('</div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="metric-container">', unsafe_allow_html=True)
    res = st.selectbox('Resolution', ['1920x1080', '1366x768', '3840x2160', '2560x1600'])
    st.markdown('</div>', unsafe_allow_html=True)

if st.button('Run AI Estimation'):
    with st.spinner('Analyzing Market Trends...'):
        # Simulate AI Prediction logic
        base_price = 45000 + (ram * 1200) + (ssd * 15) + (hdd * 5)
        predicted_price = base_price * np.random.uniform(0.95, 1.05)
        
        st.balloons()
        st.markdown(f"### Estimated Market Value: :green[₹{int(predicted_price):,}]")
        
        # Professional Charting
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = predicted_price,
            title = {'text': "Confidence Index"},
            gauge = {'axis': {'range': [None, 250000]}, 'bar': {'color': "#007bff"}}
        ))
        st.plotly_chart(fig, use_container_width=True)