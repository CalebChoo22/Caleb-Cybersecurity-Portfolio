📄 Overview

In this project, I built an AI-powered risk scoring system to automatically assess and score third-party vendors based on cybersecurity and business risk factors. It uses a simple machine learning model to predict vendor risk levels, helping organizations streamline their GRC (Governance, Risk, Compliance) and third-party risk management processes.

The project simulates real-world vendor evaluations, incorporating factors like security ratings, breach history, vulnerability counts, and industry sensitivity levels.

🚀 Features • Data Preprocessing (cleaning categorical data into model-ready format) • Risk Scoring Model using Random Forest Classifier • Threat Intelligence • Vendor Risk Predictions

🛠️ Tools and Technologies • Python (Data analysis and machine learning) • Google Colab (No setup required) • Pandas (Data handling) • CSV Data (Vendor dataset)

📂 Project Structure vendor_data_Sheet1.csv # Vendor data file (input) risk_scoring_engine.ipynb # Main Google Colab notebook

📊 How It Works 1. Vendor Dataset A simple CSV file simulates vendors with risk-related fields: • Data Breach History (Yes/No) • Security Rating (0-100) • Number of Open Vulnerabilities • Industry Sensitivity (Low/Medium/High) 2. Preprocessing Categorical data is mapped to numerical values to prepare for machine learning. 3. Risk Model A Random Forest Classifier is trained to predict whether a vendor is High Risk or Low Risk based on their profile. 4. Risk Prediction New vendor entries are automatically scored without manual analysis. 5. (Optional) Streamlit Web App A simple dashboard allows users to upload CSVs and view vendor risk levels directly online.

📥 Setup Instructions (Beginner-Friendly) 1. Open Google Colab. 2. Upload vendor_data.csv. 3. Open risk_scoring_engine.ipynb. 4. Run all cells in order. 5. To use Streamlit: • Install Streamlit (!pip install streamlit) • Upload and run app.py locally or deploy using Streamlit Cloud.

📈 Future Improvements • Integrate real-time threat feeds (e.g., AlienVault OTX API). • Expand risk factors (e.g., financial health, geographic risk). • Implement a risk scoring algorithm instead of binary classification. • Add vendor risk history and trend analysis.

🎯 Why This Project Matters • Demonstrates practical AI automation in GRC. • Bridges cybersecurity threat intelligence and machine learning. • Simulates real-world third-party risk management processes. • Beginner-friendly but portfolio-ready for internship applications in cybersecurity, GRC, SOC, and TPRM.

🧠 Skills Showcased • Data Preprocessing • Supervised Machine Learning • Cybersecurity Risk Analysis • Threat Intelligence Awareness • Python Development • Light Process Automation
