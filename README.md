# Texpedition-PrivAIlegiance
Prototype Of MVP of PrivAIlegiance 
# 🧠 PrivAIlegiance – Responsible AI-Powered Marketing Assistant

PrivAIlegiance is a privacy-first AI personalization assistant built as part of Epsilon's **TeXpedition 2025 Hackathon**.  
It empowers users by giving them control over their data, generating transparent marketing messages, and ensuring ethical AI practices.

---

## 🔍 Problem Statement

> How can AI-powered marketing systems deliver personalized experiences **without compromising user trust, data privacy, or legal compliance**?

---

## ✅ What It Does

- 📋 Lets users provide **name** and **interest**
- ✅ Allows users to **consent** to how data is used
- ✨ Generates **personalized messages** using rule-based logic
- 💬 Shows a clear **explanation** of why the message was shown
- 🔒 Displays a **privacy risk level** (🟢/🟡/🔴)
- 🧾 Simulates **GDPR/DPDP compliance checks**
- 🗂️ Logs all interactions in a **CSV file**
- 🧑‍💻 Optional admin dashboard to view logs

---

## 🚀 Features

| Module                     | Description                                      |
|----------------------------|--------------------------------------------------|
| Input Form                | Collects name and interest                      |
| Consent Engine            | User-controlled checkboxes for data usage       |
| Personalization Engine    | Generates a message using basic rules           |
| Explanation Generator     | Displays rationale behind message               |
| Privacy Risk Meter        | Displays risk score based on consent            |
| Compliance Simulation     | Simulates legal compliance messaging            |
| CSV Logger                | Saves logs for audit and traceability           |
| Admin Dashboard (optional)| View logs in `admin.py`                         |

---

## 🧰 Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **Logging**: Pandas + CSV  
- **AI (Future)**: OpenAI GPT (via `openai` SDK)  
- **Hosting (optional)**: Streamlit Cloud or Render

---

File structure
PrivAIlegiance/
├── app.py           # Main application
├── admin.py         # Optional log viewer
├── logs.csv         # Auto-generated log file
└── README.md        # You're reading this

---
🎯 Future Enhancements
🔗 Integrate OpenAI GPT for smarter message generation
📊 Add SHAP-based model explainability
🔐 Encrypt logs and add user login
📤 Export messages to email/CRM pipelines
☁️ Deploy via Streamlit Share or Render

👥 Team Name: PrivAIlegiance
Hackathon: Epsilon TeXpedition 2025
Team Members: B.M. Madhuchandra
              Chinmaya Kagolli

