import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from google.colab import files

# Upload vendor data
print("Please upload your vendor CSV file:")
uploaded = files.upload()

for filename in uploaded.keys():
    print(f"\n✅ Uploaded file: {filename}")

    # Read the CSV file
    vendor_data = pd.read_csv(filename)

    # Clean column names (remove whitespace)
    vendor_data.columns = vendor_data.columns.str.strip()

    # Show column names to debug mismatch
    print("\n🔎 Column Names:")
    print(vendor_data.columns.tolist())

    # Rename columns if necessary to match expected format
    vendor_data = vendor_data.rename(columns={
        'Breach History': 'Data Breach History',
        'Vulnerability Count': 'Number of Open Vulnerabilities',
        'Industry Sensitivity': 'Industry Sensitivity Level',
        'Vendor Name': 'Vendor'
    })

    # Show original data
    print("\n📊 --- Original Vendor Data ---")
    display(vendor_data)

    # Copy for processing
    processed_data = vendor_data.copy()

    # Handle categorical variables
    if processed_data['Data Breach History'].dtype == 'object':
        processed_data['Data Breach History'] = processed_data['Data Breach History'].map({'Yes': 1, 'No': 0}).fillna(0)

    # Map industry sensitivity
    sensitivity_mapping = {'Low': 1, 'Medium': 2, 'High': 3}
    processed_data['Industry Sensitivity Level'] = processed_data['Industry Sensitivity Level'].map(sensitivity_mapping).fillna(2)

    # Create risk label
    processed_data['Risk Label'] = np.where(
        (processed_data['Security Rating'] < 70) |
        ((processed_data['Data Breach History'] == 1) & (processed_data['Number of Open Vulnerabilities'] > 5)) |
        ((processed_data['Industry Sensitivity Level'] == 3) & (processed_data['Number of Open Vulnerabilities'] > 3)),
        1,  # High risk
        0   # Low risk
    )

    # Define features and target
    feature_columns = ['Data Breach History', 'Security Rating', 'Number of Open Vulnerabilities', 'Industry Sensitivity Level']
    X = processed_data[feature_columns]
    y = processed_data['Risk Label']

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Predict risk levels
    predictions = model.predict(X)
    prediction_proba = model.predict_proba(X)

    processed_data['Risk Level'] = ['High Risk' if p == 1 else 'Low Risk' for p in predictions]
    processed_data['Risk Score'] = [round(proba[1] * 100) for proba in prediction_proba]

    # Summary
    print("\n✅ --- Vendor Risk Assessment Results ---")
    total_vendors = len(processed_data)
    high_risk_count = (processed_data['Risk Level'] == 'High Risk').sum()
    print(f"Total Vendors: {total_vendors}")
    print(f"High Risk Vendors: {high_risk_count}")
    print(f"High Risk Percentage: {high_risk_count / total_vendors * 100:.1f}%")

    # Show results
    result_cols = ['Vendor', 'Security Rating', 'Number of Open Vulnerabilities',
                   'Data Breach History', 'Industry Sensitivity Level', 'Risk Level', 'Risk Score']
    display(processed_data[result_cols])

    # Feature importance
    print("\n📌 --- Risk Factor Importance ---")
    feature_importance = pd.DataFrame({
        'Feature': feature_columns,
        'Importance': model.feature_importances_
    }).sort_values(by='Importance', ascending=False)

    display(feature_importance)

    # Plot feature importance
    plt.figure(figsize=(10, 6))
    plt.barh(feature_importance['Feature'], feature_importance['Importance'])
    plt.xlabel('Importance')
    plt.title('Risk Factor Importance')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()
