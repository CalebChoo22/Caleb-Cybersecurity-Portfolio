import streamlit as st
import pandas as pd

# Title
st.title("AI-Powered Third-Party Vendor Risk Scoring")

# Upload CSV
uploaded_file = st.file_uploader("Upload your vendor CSV file", type="csv")

if uploaded_file is not None:
    vendor_data = pd.read_csv(uploaded_file)

    # Preprocessing
    vendor_data['Data Breach History'] = vendor_data['Data Breach History'].map({'Yes': 1, 'No': 0})
    sensitivity_mapping = {'Low': 1, 'Medium': 2, 'High': 3}
    vendor_data['Industry Sensitivity Level'] = vendor_data['Industry Sensitivity Level'].map(sensitivity_mapping)

    # Temporary: Creating fake Risk labels for training
    vendor_data['Risk'] = [1 if x < 70 else 0 for x in vendor_data['Security Rating']]

    X = vendor_data[['Data Breach History', 'Security Rating', 'Number of Open Vulnerabilities', 'Industry Sensitivity Level']]
    y = vendor_data['Risk']

    # Train model
    model = RandomForestClassifier()
    model.fit(X, y)

    # Predictions
    predictions = model.predict(X)
    vendor_data['Predicted Risk'] = ['High' if p==1 else 'Low' for p in predictions]

    st.subheader("Vendor Risk Scores")
    st.dataframe(vendor_data)
else:
    st.warning("Please upload a CSV file to continue.")
