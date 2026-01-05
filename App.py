import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# Load trained model
# --------------------------------------------------
model = joblib.load("phishing_model.pkl")

st.set_page_config(
    page_title="Phishing URL Detection",
    layout="wide"
)

st.title("🔐 Phishing URL Detection System")
st.write(
    """
    This application predicts whether a URL is **Phishing** or **Legitimate**
    based on extracted URL features.
    
    **Label Meaning:**
    - `1`  → Phishing  
    - `-1` → Legitimate
    """
)

# --------------------------------------------------
# Feature-wise allowed values (from EDA)
# --------------------------------------------------
feature_options = {
    'UsingIP': [1, -1],
    'LongURL': [1, 0, -1],
    'ShortURL': [1, -1],
    'Symbol@': [1, -1],
    'Redirecting//': [1, -1],
    'PrefixSuffix-': [-1, 1],
    'SubDomains': [0, -1, 1],
    'HTTPS': [1, -1, 0],
    'DomainRegLen': [-1, 1],
    'NonStdPort': [1, -1],
    'HTTPSDomainURL': [-1, 1],
    'RequestURL': [1, -1],
    'AnchorURL': [0, -1, 1],
    'LinksInScriptTags': [-1, 0, 1],
    'ServerFormHandler': [-1, 1, 0],
    'InfoEmail': [1, -1],
    'AbnormalURL': [1, -1],
    'WebsiteForwarding': [0, 1],
    'StatusBarCust': [1, -1],
    'DisableRightClick': [1, -1],
    'UsingPopupWindow': [1, -1],
    'IframeRedirection': [1, -1],
    'AgeofDomain': [-1, 1],
    'DNSRecording': [-1, 1],
    'WebsiteTraffic': [0, 1, -1],
    'PageRank': [-1, 1],
    'GoogleIndex': [1, -1],
    'LinksPointingToPage': [1, 0, -1],
    'StatsReport': [1, -1]
}

# --------------------------------------------------
# Input section
# --------------------------------------------------
st.subheader("🔎 Enter Feature Values")

input_data = {}

cols = st.columns(3)
for idx, (feature, options) in enumerate(feature_options.items()):
    with cols[idx % 3]:
        input_data[feature] = st.selectbox(
            label=feature,
            options=options,
            index=0
        )

# Convert input to DataFrame (exact training schema)
input_df = pd.DataFrame([input_data])

# --------------------------------------------------
# Prediction
# --------------------------------------------------
if st.button("🔍 Predict"):
    prediction = model.predict(input_df)[0]

    # Probability handling (if available)
    phishing_confidence = None
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(input_df)[0]
        phishing_confidence = proba[list(model.classes_).index(1)]

    if prediction == 1:
        st.error("⚠️ Phishing URL Detected")
        if phishing_confidence is not None:
            st.write(f"Confidence: {phishing_confidence:.2%}")
    else:
        st.success("✅ Legitimate URL")
        if phishing_confidence is not None:
            st.write(f"Confidence: {(1 - phishing_confidence):.2%}")

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption(
    "Phishing URL Detection System | Streamlit Deployment | Data Science Project"
)
