!pip install pandas scikit-learn
from google.colab import files
uploaded = files.upload()

from scipy.io import arff
import pandas as pd

data, meta = arff.loadarff('Training Dataset.arff')
df = pd.DataFrame(data)
df = df.applymap(lambda x: x.decode('utf-8') if isinstance(x, bytes) else x)
print("Missing values:", df.isnull().sum().sum())

X = df.drop('Result', axis=1)
y = df['Result'].astype(int)
print(list(X.columns))

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

!pip install gradio

import gradio as gr
import numpy as np

def predict_phishing(*inputs):
    input_array = np.array(inputs).reshape(1, -1)
    prediction = model.predict(input_array)[0]
    return "Phishing Website" if prediction == -1 else "Legitimate Website"

feature_labels = ['Having_IP_Address', 'URL_Length', 'Shortening_Service', 'Having_At_Symbol',
                  'Double_slash_redirecting', 'Prefix_Suffix', 'Sub_Domain', 'SSLfinal_State',
                  'Domain_registeration_length', 'Favicon', 'port', 'HTTPS_token',
                  'Request_URL', 'URL_of_Anchor', 'Links_in_tags', 'SFH', 'Submitting_to_email',
                  'Abnormal_URL', 'Redirect', 'on_mouseover', 'RightClick', 'popUpWidnow',
                  'Iframe', 'age_of_domain', 'DNSRecord', 'web_traffic', 'Page_Rank',
                  'Google_Index', 'Links_pointing_to_page', 'Statistical_report']

inputs = [gr.Slider(minimum=-1, maximum=1, step=1, label=label) for label in feature_labels]

interface = gr.Interface(
    fn=predict_phishing,
    inputs=inputs,
    outputs="text",
    title="Phishing Website Detector",
    description="Adjust feature values to see if it's phishing or legit."
)

interface.launch()
