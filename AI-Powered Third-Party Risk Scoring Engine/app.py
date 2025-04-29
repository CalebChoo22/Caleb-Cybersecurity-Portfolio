import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="AI-Powered Third-Party Risk Scoring", layout="wide")

st.title("AI-Powered Third-Party Vendor Risk Scoring")
st.markdown("Upload your vendor data to automatically assess cybersecurity and business risk factors.")

# File uploader
uploaded_file = st.file_uploader("Upload your vendor CSV file", type=["csv"])

def preprocess_data(df):
    """Preprocess the vendor data"""
    # Create a copy to avoid modifying the original
    processed_df = df.copy()
    
    # Handle categorical variables
    if 'Data Breach History' in processed_df.columns:
        processed_df['Data Breach History'] = processed_df['Data Breach History'].map({'Yes': 1, 'No': 0})
    
    # Map industry sensitivity
    sensitivity_mapping = {'Low': 1, 'Medium': 2, 'High': 3}
    if 'Industry Sensitivity Level' in processed_df.columns:
        processed_df['Industry Sensitivity Level'] = processed_df['Industry Sensitivity Level'].map(sensitivity_mapping)
    
    return processed_df

def train_model(df):
    """Train the risk scoring model"""
    # For demonstration, we'll use security rating threshold to create labels
    # In a real implementation, you would have actual risk labels
    df['Risk Label'] = np.where(
        (df['Security Rating'] < 70) | 
        (df['Data Breach History'] == 1 & df['Number of Open Vulnerabilities'] > 5) |
        (df['Industry Sensitivity Level'] == 3 & df['Number of Open Vulnerabilities'] > 3),
        1,  # High risk
        0   # Low risk
    )
    
    # Features for the model
    X = df[['Data Breach History', 'Security Rating', 'Number of Open Vulnerabilities', 'Industry Sensitivity Level']]
    y = df['Risk Label']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    return model, accuracy

def predict_risk(model, df):
    """Predict risk scores for vendors"""
    # Get features
    X = df[['Data Breach History', 'Security Rating', 'Number of Open Vulnerabilities', 'Industry Sensitivity Level']]
    
    # Predict
    predictions = model.predict(X)
    prediction_proba = model.predict_proba(X)
    
    # Add predictions to dataframe
    df['Risk Level'] = ['High Risk' if p == 1 else 'Low Risk' for p in predictions]
    df['Risk Score'] = [round(proba[1] * 100) for proba in prediction_proba]
    
    return df

if uploaded_file is not None:
    try:
        # Load data
        vendor_data = pd.read_csv(uploaded_file)
        
        # Show original data
        st.subheader("Original Vendor Data")
        st.dataframe(vendor_data)
        
        # Check required columns
        required_columns = ['Data Breach History', 'Security Rating', 'Number of Open Vulnerabilities', 'Industry Sensitivity Level']
        missing_columns = [col for col in required_columns if col not in vendor_data.columns]
        
        if missing_columns:
            st.error(f"Missing required columns: {', '.join(missing_columns)}")
            st.stop()
        
        # Preprocess data
        processed_data = preprocess_data(vendor_data)
        
        # Train the model
        with st.spinner("Training risk scoring model..."):
            model, accuracy = train_model(processed_data)
            st.success(f"Model trained with accuracy: {accuracy:.2f}")
        
        # Predict risk scores
        risk_results = predict_risk(model, processed_data)
        
        # Display results
        st.subheader("Vendor Risk Assessment Results")
        
        # Calculate overall risk metrics
        high_risk_count = sum(risk_results['Risk Level'] == 'High Risk')
        total_vendors = len(risk_results)
        
        # Create columns for metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Vendors", total_vendors)
        col2.metric("High Risk Vendors", high_risk_count)
        col3.metric("High Risk Percentage", f"{high_risk_count/total_vendors*100:.1f}%")
        
        # Display risk results with color coding
        st.dataframe(
            risk_results[['Vendor', 'Security Rating', 'Number of Open Vulnerabilities', 
                         'Data Breach History', 'Industry Sensitivity Level', 'Risk Level', 'Risk Score']]
            .style.apply(lambda x: ['background-color: #ffcccc' if x['Risk Level'] == 'High Risk' 
                                   else 'background-color: #ccffcc' for i in x], axis=1)
        )
        
        # Feature importance
        st.subheader("Risk Factor Importance")
        feature_importance = pd.DataFrame({
            'Feature': required_columns,
            'Importance': model.feature_importances_
        }).sort_values('Importance', ascending=False)
        
        st.bar_chart(feature_importance.set_index('Feature'))
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.info("Please ensure your CSV file has the required columns: 'Vendor', 'Data Breach History', 'Security Rating', 'Number of Open Vulnerabilities', and 'Industry Sensitivity Level'")

else:
    # Display sample format when no file is uploaded
    st.info("Please upload a CSV file with vendor data to begin the risk assessment.")
    
    st.subheader("Sample CSV Format")
    sample_data = pd.DataFrame({
        'Vendor': ['Vendor A', 'Vendor B', 'Vendor C'],
        'Data Breach History': ['Yes', 'No', 'No'],
        'Security Rating': [60, 85, 90],
        'Number of Open Vulnerabilities': [12, 2, 0],
        'Industry Sensitivity Level': ['High', 'Medium', 'Low']
    })
    
    st.dataframe(sample_data)
    
    # Provide download link for sample template
    @st.cache_data
    def convert_df_to_csv(df):
        return df.to_csv(index=False).encode('utf-8')
    
    csv = convert_df_to_csv(sample_data)
    st.download_button(
        label="Download Sample Template",
        data=csv,
        file_name="vendor_data_template.csv",
        mime="text/csv",
    )
