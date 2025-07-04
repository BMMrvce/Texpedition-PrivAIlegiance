import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="PrivAIlegiance – Admin Logs", page_icon="🗂️")
st.title("📊 PrivAIlegiance – Consent Log Viewer")

# Check if logs.csv exists
log_file = "logs.csv"

if os.path.exists(log_file):
    df = pd.read_csv(log_file, names=["Timestamp", "Name Used", "Interest Used", "Message"])
    
    st.success(f"✅ {len(df)} log entries found.")
    st.dataframe(df)

    # Optional: filter logs
    st.markdown("### 🔍 Filter Logs")
    name_filter = st.text_input("Filter by message content or keywords:")
    if name_filter:
        filtered_df = df[df["Message"].str.contains(name_filter, case=False)]
        st.write(f"Found {len(filtered_df)} results:")
        st.dataframe(filtered_df)

    # Optional: download filtered or full logs
    st.download_button(
        label="📥 Download Logs as CSV",
        data=df.to_csv(index=False),
        file_name="privAIlegiance_logs.csv",
        mime="text/csv"
    )

else:
    st.warning("⚠️ No logs found. Run the main app and generate at least one entry.")
