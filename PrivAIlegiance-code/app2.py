import streamlit as st
import pandas as pd
from datetime import datetime

# Page setup
st.set_page_config(page_title="PrivAIlegiance", page_icon="🤖")
st.title("🤖 PrivAIlegiance – Ethical AI Marketing Assistant")
st.markdown("Ensure AI-powered personalization with transparency and privacy compliance.")

# User Inputs
st.header("🔍 User Information")
name = st.text_input("Enter your name:")
interest = st.text_input("Enter your interest (e.g., sports, fashion, tech):")

st.header("🔐 Consent Preferences")
use_name = st.checkbox("Allow use of name", value=True)
use_interest = st.checkbox("Allow use of interest", value=True)

# Button to generate message
if st.button("Generate Personalized Message"):
    st.subheader("🧠 Personalized Output")

    # Logic to generate message
    if use_name and use_interest:
        message = f"Hi {name}, check out the latest in {interest}! 🛍️"
        explanation = f"You received this because your interest is '{interest}' and your name was used for personalization."
    elif use_interest:
        message = f"Explore the latest in {interest}, just for you!"
        explanation = f"This was shown based on your interest: {interest}."
    elif use_name:
        message = f"Hi {name}, explore what's new and trending today!"
        explanation = f"Message generated using your name only."
    else:
        message = "Generic message: Explore our latest offers."
        explanation = "No personal data was used in this message."

    # Display message and explanation
    st.success(message)
    st.write("📌", explanation)

    # Privacy Risk Meter
    st.markdown("### 🔒 Privacy Risk Indicator")
    if use_name and use_interest:
        st.warning("🔴 High Privacy Risk – Both name and interest used.")
    elif use_name or use_interest:
        st.info("🟡 Medium Privacy Risk – Partial personal data used.")
    else:
        st.success("🟢 Low Privacy Risk – No personal data used.")

    # Compliance Simulation
    st.markdown("### 🧾 Compliance Status")
    if use_name or use_interest:
        st.success("✅ Message complies with GDPR/DPDP based on user consent.")
    else:
        st.info("ℹ️ Fully compliant: no personal data used.")

    # Save log to CSV
    log = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "name_used": use_name,
        "interest_used": use_interest,
        "message": message
    }

    df = pd.DataFrame([log])
    df.to_csv("logs.csv", mode="a", index=False, header=False)

    st.markdown("✅ Log entry saved.")
