import streamlit as st
import requests
import hashlib
import fitz  # PyMuPDF for PDF text extraction
from cryptography.fernet import Fernet
import os

# ------------------ Security: Encryption for Data Privacy ------------------
KEY_FILE = "encryption.key"

def load_encryption_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
    with open(KEY_FILE, "rb") as key_file:
        return Fernet(key_file.read())

cipher = load_encryption_key()

def encrypt_data(data):
    return cipher.encrypt(data.encode()).decode()

# ------------------ Resume Upload & Text Extraction ------------------
def extract_text_from_pdf(file):
    pdf_reader = fitz.open(stream=file.read(), filetype="pdf")
    text = "\n".join(page.get_text() for page in pdf_reader)
    return text[:1000]  

# ------------------ AI API Configuration ------------------
HF_API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
HF_HEADERS = {"Authorization": "Bearer Enter your api key"}  # Replace with your key

# ------------------ AI: Generate Interview Questions ------------------
def generate_questions(tech_stack, experience, position):
    prompt = f"Generate 3 technical interview questions for a {experience}-year experienced candidate applying for {position} skilled in {tech_stack}."
    response = requests.post(HF_API_URL, headers=HF_HEADERS, json={"inputs": prompt})
    
    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list) and len(result) > 0 and "generated_text" in result[0]:
            questions = result[0]["generated_text"].split("\n")
        else:
            questions = ["Error: Could not generate questions."]
        return [q.strip() for q in questions[:3] if q]
    return [f"Error: {response.status_code} - {response.text}"]

# ------------------ AI: Sentiment Analysis ------------------
def analyze_sentiment(answer):
    prompt = f"Analyze the sentiment of the following interview answer and return a summary: {answer}"
    response = requests.post(HF_API_URL, headers=HF_HEADERS, json={"inputs": prompt})
    
    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    return "Error analyzing sentiment."

# ------------------ UI: Streamlit Web App ------------------
st.set_page_config(page_title="Intelligent Hiring Assistant", page_icon="🤖", layout="centered")

# ---- Styling ----
st.markdown("""
    <style>
        .stTextArea textarea { border-radius: 10px; border: 2px solid #4CAF50; padding: 10px; }
        .stMarkdown { font-size: 18px; font-weight: bold; }
        .stButton>button { background-color: #4CAF50; color: white; font-size: 16px; border-radius: 10px; padding: 10px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("## 🤖 Intelligent Hiring Assistant")
st.markdown("👋 **Hello! Let's start your interview process.**")

# Exit Option
exit_keywords = ["exit", "quit", "stop"]
user_exit_input = st.text_input("Type 'exit' anytime to quit", key="exit")
if user_exit_input.lower().strip() in exit_keywords:
    st.warning("👋 Thank you for using the hiring assistant. Have a good Day!")
    st.stop()

with st.form("candidate_form"):
    st.subheader("📋 Candidate Details")
    name = st.text_input("Full Name", key="name")
    email = st.text_input("Email", key="email")
    phone = st.text_input("Phone Number", key="phone")
    experience = st.number_input("Years of Experience", min_value=0, step=1, key="experience")
    tech_stack = st.text_input("Tech Stack (e.g., Python, AWS, Machine Learning)", key="tech_stack")
    position = st.text_input("Position Applied For", key="position")
    tech_stack = st.text_input("Tech Stack (e.g., Python, AWS, Machine Learning)", key="tech_stack")
    resume = st.file_uploader("Upload Resume (PDF only)", type=["pdf"], key="resume")

    submitted = st.form_submit_button("Submit")

if submitted:
    if not position.strip():
        st.warning("⚠️ Please enter the position before proceeding.")
    else:
        # Encrypt candidate details
        candidate_info = {
            "name": encrypt_data(name),
            "email": encrypt_data(email),
            "phone": encrypt_data(phone),
            "experience": experience,
            "tech_stack": tech_stack,
            "position": position
        }
        
        # Extract text from resume
        if resume:
            extracted_text = extract_text_from_pdf(resume)
            st.text_area("📄 Extracted Resume Content (Preview)", extracted_text, height=150)

        # Generate interview questions
        st.session_state.questions = generate_questions(tech_stack, experience, position)

# ---- Display Questions & Answer Input ----
if "questions" in st.session_state and st.session_state.questions:
    st.subheader("📝 Interview Questions")
    answers = {}

    for i, question in enumerate(st.session_state.questions, 1):
        if question:
            st.markdown(f"**❓ Question {i}:** {question}")  # Display question as read-only text
            answers[f"Q{i}"] = st.text_area(f"✍️ Your Answer {i}", key=f"answer_{i}")  # Answer input box

    if st.button("Analyze Responses"):
        st.subheader("📊 Sentiment Analysis")
        for key, answer in answers.items():
            sentiment = analyze_sentiment(answer)
            st.write(f"✅ {key}: {sentiment}")

# ---- Data Privacy Notice ----
st.markdown("🔒 **Data Privacy Notice:** Your data is encrypted and used only for interview assessment. No personal information is stored permanently.")