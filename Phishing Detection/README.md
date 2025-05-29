#  Phishing Website Detector

This project predicts whether a website is phishing or legitimate based on 30 different features. It’s built in Python and uses a real dataset from UCI.

---

## What This Does

- Trains a random model on a real phishing dataset
- Predicts if a website is safe or suspicious using its characteristics (like if it uses an IP address, has HTTPS, how long the domain has existed, etc.)
- There is also a website that generates where you can use sliders to determine if it's phishing or not.

---

##  How It Works

1. I used the UCI Phishing Websites Dataset, which includes 30 features and labels for thousands of websites.
2. Each feature is categorized as:
   - `-1` = suspicious
   - `0` = uncertain
   - `1` = safe
   
---

## Tools I used

- Python (with Pandas and Scikit-learn)
- Gradio (for UI)
- Google Colab (for writing code)
- UCI Phishing Dataset (real-world data found online)

---

##  Example Prediction

Here’s what using it looks like:

- You set sliders like:
  - `Having_IP_Address = -1`
  - `URL_Length = -1`
  - `SSLfinal_State = 1`
- Click "Submit"
- The model will tell you:
  > “Phishing Website” or “Legitimate Website”

---

## Resources:
- [UCI Phishing Dataset](https://archive.ics.uci.edu/ml/datasets/Phishing+Websites)
- [Gradio](https://gradio.app/)
- Google Colab
