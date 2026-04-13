import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Bioprocess Digital Twin", layout="wide")

# -------------------------
# TITLE
# -------------------------
st.title("🧬 Bioprocess Digital Twin with Causal AI")
st.markdown("Interactive simulation + ML + causal reasoning")

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.header("⚙️ Process Controls")

temperature = st.sidebar.slider("Temperature (°C)", 30.0, 45.0, 37.0)
ph = st.sidebar.slider("pH", 5.5, 8.5, 7.0)
nutrients = st.sidebar.slider("Nutrients", 0.0, 120.0, 80.0)

# -------------------------
# FUNCTIONS
# -------------------------
def compute_biomass(temp, ph, nutrients):
    return 0.5 * nutrients + 2 * temp - 3 * abs(ph - 7)

def predict_product(biomass):
    return 0.8 * biomass + np.random.normal(0, 2)

biomass = compute_biomass(temperature, ph, nutrients)
product = predict_product(biomass)

# -------------------------
# TABS
# -------------------------
tab1, tab2, tab3 = st.tabs(["📊 Simulation", "📈 Analytics", "🧠 Causal Graph"])

# -------------------------
# TAB 1: SIMULATION
# -------------------------
with tab1:
    st.subheader("Real-Time Outputs")

    col1, col2 = st.columns(2)
    col1.metric("Biomass", f"{biomass:.2f}")
    col2.metric("Product Yield", f"{product:.2f}")

# -------------------------
# TAB 2: ANALYTICS
# -------------------------
with tab2:
    st.subheader("Time-Series Simulation")

    time = np.arange(100)
    products = [predict_product(biomass) for _ in time]

    df = pd.DataFrame({"time": time, "product": products})
    st.line_chart(df.set_index("time"))

    st.subheader("Feature Influence (Heuristic)")
    st.write({
        "Temperature Impact": "High",
        "pH Stability": "Critical",
        "Nutrients": "Primary Driver"
    })

# -------------------------
# TAB 3: CAUSAL DAG
# -------------------------
with tab3:
    st.subheader("Causal Relationships (DAG)")

    st.markdown("""
    ```
        Nutrients → Biomass → Product
        Temperature → Biomass
        pH → Biomass
        Temperature → Product
    ```
    """)

    st.info("Causal graph helps identify root causes, not just correlations.")

# -------------------------
# INSIGHTS
# -------------------------
st.subheader("🧠 Insights")

if temperature > 40:
    st.warning("High temperature → possible instability")

if abs(ph - 7) > 0.5:
    st.warning("pH deviation → impacts growth")

if nutrients < 20:
    st.warning("Low nutrients → reduced output")

st.success("System operating within optimal range")

# -------------------------
# FOOTER
# -------------------------
st.markdown("---")
st.markdown("Built by Subhankar Biswas | Digital Twin + Causal AI🚀")