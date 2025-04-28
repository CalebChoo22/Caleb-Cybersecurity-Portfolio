import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.title("AI-Powered Third-Party Vendor Risk Scoring")

# Upload the CSV file
uploaded_file = st.file_uploader("Upload your vendor CSV file", type=["csv"])

if uploaded_file is not None:
    vendor_data = pd.read_csv(uploaded_file)

    # Preprocessing
    vendor_data['Data Breach History'] = vendor_data['Data Breach History'].map({'Yes': 1, 'No': 0})
    sensitivity_mapping = {'Low': 1, 'Medium': 2, 'High': 3}
    vendor_data['Industry Sensitivity Level'] = vendor_data['Industry Sensitivity Level'].map(sensitivity_mapping)

    # Temporary: Creating fake Risk labels (based on security rating)
    vendor_data['Risk'] = [1 if rating < 70 else 0 for rating in vendor_data['Security Rating']]

    # Features and Target
    X = vendor_data[['Data Breach History', 'Security Rating', 'Number of Open Vulnerabilities', 'Industry Sensitivity Level']]
    y = vendor_data['Risk']

    # Train the model
    model = RandomForestClassifier()
    model.fit(X, y)

    # Predict
    predictions = model.predict(X)
    vendor_data['Predicted Risk'] = ['High' if p == 1 else 'Low' for p in predictions]

    st.subheader("Vendor Risk Scores")
    st.dataframe(vendor_data)

else:
    st.warning("Please upload a CSV file to continue.")