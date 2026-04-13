import streamlit as st
import pandas as pd
import numpy as np
import torch
from sklearn.preprocessing import StandardScaler

# -------------------------
# Title
# -------------------------
st.set_page_config(page_title="Bioprocess Digital Twin", layout="wide")

st.title("🧬 Bioprocess Digital Twin with Causal AI")
st.markdown("Interactive simulation of bioreactor process dynamics")

# -------------------------
# Sidebar Inputs
# -------------------------
st.sidebar.header("⚙️ Process Parameters")

temperature = st.sidebar.slider("Temperature (°C)", 30.0, 45.0, 37.0)
ph = st.sidebar.slider("pH Level", 5.5, 8.5, 7.0)
nutrients = st.sidebar.slider("Nutrient Level", 0.0, 120.0, 80.0)

# -------------------------
# Simulated Biomass Function
# -------------------------
def compute_biomass(temp, ph, nutrients):
    return 0.5 * nutrients + 2 * temp - 3 * abs(ph - 7)

biomass = compute_biomass(temperature, ph, nutrients)

# -------------------------
# Simple Model (Mock or Load PyTorch)
# -------------------------
def predict_product(temp, ph, nutrients, biomass):
    return 0.8 * biomass + np.random.normal(0, 2)

product = predict_product(temperature, ph, nutrients, biomass)

# -------------------------
# Display Results
# -------------------------
st.subheader("📊 Predicted Outputs")

col1, col2 = st.columns(2)

with col1:
    st.metric("Biomass", f"{biomass:.2f}")

with col2:
    st.metric("Product Yield", f"{product:.2f}")

# -------------------------
# Visualization
# -------------------------
st.subheader("📈 Process Simulation")

time = np.arange(50)
simulated_product = [
    predict_product(temperature, ph, nutrients, biomass) for _ in time
]

df = pd.DataFrame({
    "time": time,
    "product": simulated_product
})

st.line_chart(df.set_index("time"))

# -------------------------
# Insights Section
# -------------------------
st.subheader("🧠 Insights")

if temperature > 40:
    st.warning("High temperature detected → may negatively impact process stability")

if abs(ph - 7) > 0.5:
    st.warning("pH deviation detected → affects biomass growth")

if nutrients < 20:
    st.warning("Low nutrients → limited biomass production")

st.success("Model suggests stable operation within optimal ranges")

# -------------------------
# Footer
# -------------------------
st.markdown("---")
st.markdown("Built by Subhankar Biswas | Digital Twin + Causal AI")