Cybersecurity Risk Assessment – Capital One

Overview

I created a simulated cybersecurity risk assessment of Capital One. It demonstrates risk analysis using publicly available information. The goal is to identify and evaluate cyber threats and vulnerabilities affecting key IT assets, calculate risk levels, and recommend appropriate mitigation controls.

I based this assessment on the NIST SP 800-30 risk management framework. Each asset is evaluated for potential threats and vulnerabilities, and risk scores are calculated using a Likelihood × Impact model on a scale of 1 to 5. The assessment covers five critical IT assets, including cloud infrastructure, mobile applications, administrative portals, APIs, and email systems.

Risk scores were determined based on publicly known incidents. For example, Capital One’s 2019 data breach due to misconfigured AWS S3 buckets informs both the likelihood and impact scoring in this simulation.

Key Findings
	•	The AWS S3 misconfiguration risk was scored as critical due to its high likelihood and severe impact.
	•	Insider threats from administrative portal misuse and phishing attacks against employees were also identified as high risks.
	•	API and mobile app vulnerabilities were moderate but still relevant to the organization’s cybersecurity posture.


Some things I recommended based on risk severity were to implement multifactor authentication (MFA), apply least privilege access models, conduct quarterly access reviews, secure APIs, and increase phishing awareness through employee training.

This project is a simulation based on public information.
