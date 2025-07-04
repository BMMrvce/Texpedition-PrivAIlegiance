import streamlit as st

st.set_page_config(page_title="PrivAIlegiance", page_icon="🤖")

st.title("🤖 PrivAIlegiance - Ethical AI Marketing Assistant")

# Form inputs
name = st.text_input("Enter your name")
interest = st.text_input("Enter your interest (e.g., sports, fashion)")

st.write("### 🔐 Consent Preferences")
use_name = st.checkbox("Allow use of name")
use_interest = st.checkbox("Allow use of interest")

# On button click
if st.button("Generate Personalized Message"):
    if use_name and use_interest:
        message = f"Hi {name}, check out the latest in {interest}! 🛍️"
        explanation = f"You received this because your interest is '{interest}'."
    elif use_interest:
        message = f"Explore the latest in {interest} curated just for you!"
        explanation = f"This message is based on your selected interest: {interest}."
    elif use_name:
        message = f"Hi {name}, explore our trending collections!"
        explanation = f"Generated using your name input only."
    else:
        message = "Please enable at least one data input for personalization."
        explanation = ""

    st.markdown("---")
    st.subheader("🧠 Personalized Message")
    st.success(message)
    st.write("📌", explanation)
    st.markdown("✅ This message complies with data privacy policies (GDPR / DPDP).")

