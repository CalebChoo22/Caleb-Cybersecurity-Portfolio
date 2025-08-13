Automated NIST 800-53 Control Gap Assessment Tool

Overview

I built this tool that automates a basic NIST SP 800-53 control gap analysis, simulating the type of compliance and risk assessment work done in Governance, Risk, and Compliance (GRC) teams.

It takes in:
	•	A CSV of security controls (sample from NIST 800-53)
	•	A CSV of implementation evidence (mock policies, procedures, and links)

The script then:
	•	Flags controls as Compliant or Gap
	•	Assigns a High/Medium/Low risk tier based on control family
Generates:
	•	gap_report.csv → detailed results for each control
	•	summary.txt → compliance percentage, gap counts, and “quick win” recommendations

Features
	•	Automates control/evidence cross-checking for compliance
	•	Simple risk tiering logic based on control families
	•	Generates clear, exportable reports for review or presentation
