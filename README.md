# 🧬 Bioprocess Digital Twin with Causal AI

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-DeepLearning-red)
![Causal AI](https://img.shields.io/badge/Causal%20AI-DoWhy-green)
![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🚀 Overview
This project implements a **Bioprocess Digital Twin** integrating:

- 🔁 Time-series simulation of a bioreactor system  
- 🤖 Deep learning using PyTorch  
- 🧠 Causal inference using DoWhy  

It models relationships between:
- Temperature  
- pH  
- Nutrients  
- Biomass  
- Product yield  

---

## 🧠 Architecture

![Architecture](diagrams/architecture.png)

---

## 🔬 Key Features

### 🧪 Digital Twin Simulation
- Synthetic bioprocess data generation  
- Time-dependent system dynamics  

### 🤖 Deep Learning Model
- PyTorch neural network  
- Predicts product yield  

### 🧬 Causal AI
- DAG-based causal modeling  
- Root cause analysis using DoWhy  

---

## 📊 Example Workflow

```bash
python src/simulation.py
python src/train.py
python src/causal.py

🛠 Tech Stack
Python
PyTorch
Pandas, NumPy
Scikit-learn
DoWhy

📈 Results
Captured process dynamics via ML
Identified causal impact of temperature on production
Simulated batch deviations

📌 Project Structure
bioprocess-digital-twin/
│
├── data/
├── notebooks/
├── src/
├── diagrams/
├── requirements.txt
└── README.md

🎯 Relevance
✔ Digital Twin Modeling
✔ Bioprocess Data Science
✔ Causal AI for Root Cause Analysis
✔ Time-Series + High-Dimensional Data

🚀 Future Improvements
Real bioprocess datasets
Reinforcement learning optimization
Advanced causal discovery

👤 Author
Subhankar Biswas
MSc Data Engineering
GitHub: https://github.com/Subiswas36218/bioprocess-digital-twin-causal-ai