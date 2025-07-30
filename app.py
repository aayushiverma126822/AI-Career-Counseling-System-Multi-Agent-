# app.py

import streamlit as st
import google.generativeai as genai

# Load your API key securely from Streamlit secrets
genai.configure(api_key=st.secrets["AIzaSyBT_YwE11vpusexvce8Vn76KuvWsvqNyIA"])

# Then use Gemini in your logic
response = genai.GenerativeModel("gemini-pro").generate_content("Hello!")
st.write(response.text)


import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Career Counselor", layout="centered")

# Load Gemini API key
genai.configure(api_key=st.secrets["AIzaSyBT_YwE11vpusexvce8Vn76KuvWsvqNyIA"])

model = genai.GenerativeModel("gemini-pro")

st.title("🤖 AI Career Counseling System")

resume = st.text_area("Paste your resume text here:")
if st.button("Analyze Resume"):
    with st.spinner("Analyzing..."):
        prompt = f"Based on this resume, suggest 3 suitable job roles:\n\n{resume}"
        response = model.generate_content(prompt)
        st.subheader("Suggested Roles:")
        st.write(response.text)
