import streamlit as st
import google.generativeai as genai
from cryptography.fernet import Fernet
import os

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


# Configure Gemini API
genai.configure(api_key="Enter your Gemini API Key")

# Function to generate structured technical questions
def generate_questions(tech_stack):
    prompt = (
        f"Generate exactly 3 to 5 concise technical interview questions based on these technologies: {', '.join(tech_stack)}. "
        "Ensure the response is a numbered list with one question per line. Keep questions short and relevant."
    )
    response = genai.GenerativeModel("gemini-pro").generate_content(prompt)
    
    if response and response.text:
        questions = response.text.split("\n")
        return [q.strip() for q in questions if q.strip()]
    return []

# Function to generate chatbot response dynamically
def chatbot_response(user_input):
    if user_input.lower() in ["stop", "exit", "quit"]:
        return "Thank you for your time! We'll be in touch soon. 😊"

    prompt = f"Act as an AI interview assistant. Respond concisely to: {user_input}"
    response = genai.GenerativeModel("gemini-pro").generate_content(prompt)
    
    return response.text if response else "I'm sorry, I couldn't process that."

# UI Styling
st.markdown(
    """
    <style>
        .title { font-size: 40px; font-weight: bold; color: cyan; text-align: center; }
        .subtitle { font-size: 20px; font-weight: bold; color: red; margin-top: 20px; }
        .question { font-size: 18px; font-weight: bold; margin-top: 10px; }
        .chat-bubble { background-color: red; padding: 10px; border-radius: 10px; margin: 5px 0; }
        .bot-response { background-color: green; padding: 10px; border-radius: 10px; margin: 5px 0; }
        .answer-box { width: 100%; height: 50px; font-size: 16px; }
        .submit-btn {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border: none;
            padding: 10px;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 10px;
        }
        .submit-btn:hover { background-color: #45a049; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Greeting
st.markdown('<p class="title">🤖 TalentScout Recruitment Chatbot</p>', unsafe_allow_html=True)
st.markdown("👋 **Hello! Let's start your interview process.**")
st.write("Please provide your details to proceed with the interview.")

# Collect Candidate Details
full_name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
experience = st.number_input("Years of Experience", min_value=0, step=1, key="experience")
position = st.text_input("Desired Position")
location = st.text_input("Current Location")

# Tech Stack Declaration
tech_stack = st.text_area("Enter your tech stack (comma-separated)", placeholder="E.g., Python, Django, MySQL, React")

# Generate Questions
if st.button("Generate Questions"):
    if tech_stack:
        tech_list = [tech.strip() for tech in tech_stack.split(",")]
        questions = generate_questions(tech_list)

        if questions:
            st.markdown('<p class="subtitle">Your Technical Questions</p>', unsafe_allow_html=True)
            answers = {}
            for i, question in enumerate(questions[:5], 1):  # Max 5 questions
                st.markdown(f'<p class="question">Q{i}: {question}</p>', unsafe_allow_html=True)
                answers[f"answer_{i}"] = st.text_area(f"Answer {i}", key=f"answer_{i}")
            
            if st.button("Submit Answers"):
                st.success("Your responses have been submitted successfully! ✅")
        else:
            st.warning("Could not generate questions. Please try again.")
    else:
        st.warning("Please enter your tech stack before generating questions.")

# Chatbot Section
st.markdown("---")
st.markdown('<p class="subtitle">💬 Chat with AI Assistant</p>', unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

user_input = st.text_input("Type your message here...")

if user_input:
    bot_reply = chatbot_response(user_input)
    st.session_state["chat_history"].append(("You", user_input))
    st.session_state["chat_history"].append(("Bot", bot_reply))

# Display Chat History
for sender, message in st.session_state["chat_history"]:
    if sender == "You":
        st.markdown(f'<div class="chat-bubble"><strong>{sender}:</strong> {message}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-response"><strong>{sender}:</strong> {message}</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("⚠️ **Data Privacy & Compliance**: This chatbot follows GDPR compliance by not storing any real candidate data.")