In this project, I built a risk scoring system to automatically assess and score third-party vendors based on their business risk factors. It predicts vendor risk levels, helping organizations with their GRC and third-party risk management processes.

Features • Data Preprocessing • Risk Scoring Model • Threat Intelligence • Vendor Risk Predictions

How It Works
1. Vendor Dataset - A simple CSV file simulates vendors with risk-related fields: • Data Breach History (Yes/No) • Security Rating (0-100) • Number of Open Vulnerabilities • Industry Sensitivity (Low/Medium/High)
2. Preprocessing - Categorical data is mapped to numerical values to prepare for machine learning.
3. Risk Model - A Classifier is trained to predict whether a vendor is High Risk or Low Risk based on their profile.
4. Risk Prediction - New vendor entries are automatically scored without manual analysis.
