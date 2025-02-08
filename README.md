# PGAG
Chatbot demo link using LOOM:https://www.loom.com/share/6d60b536d80d4a7f8fa1e5837a733dfa?sid=e9695d4b-8fc2-4926-8b19-aa07d1de9306

📌 Intelligent Hiring Assistant

📝 Project Overview

The Intelligent Hiring Assistant is a chatbot designed to streamline the interview process by generating tailored technical interview questions, allowing candidates to input their answers, and performing sentiment analysis to assess responses. The chatbot also provides basic resume analysis and ensures data privacy through encryption.

⚡ Features

📄 Resume Text Extraction (PDF support)

🤖 AI-powered Interview Question Generation

📝 Candidate Answer Collection

📊 Sentiment Analysis of Responses

🔐 Data Encryption for Privacy Protection

🚀 User-Friendly Streamlit Interface

📥 Installation Instructions

🔧 Prerequisites

Ensure you have the following installed:

Python 3.8+

pip (Python package manager)

🛠️ Setup Steps

Clone the Repository:

git clone https://github.com/your-repo/hiring-assistant.git
cd hiring-assistant

Create a Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Required Dependencies:

pip install -r requirements.txt

Set Up API Keys:

Obtain a Hugging Face API key from Hugging Face.

Replace the placeholder key in app.py:

HF_HEADERS = {"Authorization": "Bearer YOUR_HUGGINGFACE_API_KEY"}

Run the Application:

streamlit run app.py

🎯 Usage Guide

Start the application by running streamlit run app.py.

Fill out the candidate details (Name, Email, Experience, Tech Stack, etc.).

Upload a PDF resume (optional) for text extraction.

Get AI-generated technical interview questions.

Provide answers in separate text areas.

Analyze sentiment of responses using AI.

Review the analysis and insights.

🏗️ Technical Details

📚 Libraries Used

Streamlit (User Interface)

Requests (API calls)

Fitz (PyMuPDF) (PDF Text Extraction)

Cryptography (Fernet) (Encryption)

Hugging Face Transformers (AI Processing)

🏛️ Architectural Decisions

Why Streamlit? Quick prototyping, interactive UI, and lightweight.

Why Hugging Face? Free-tier model access, scalable inference API.

Why Encryption? To ensure candidate privacy and security.

✍️ Prompt Design

Information Gathering: The AI receives candidate details and crafts specific technical interview questions.

Question Generation: The AI is prompted to generate tailored interview questions based on experience, tech stack, and role.

Sentiment Analysis: The AI assesses positivity, confidence, and technical depth in candidate responses.

Example prompt:

Generate 3 technical interview questions for a [Experience] years experienced candidate applying for [Position] skilled in [Tech Stack].

🛠️ Challenges & Solutions

🚧 Challenges Faced

Question Format Issues:

AI sometimes returned questions in a block of text.

Solution: Used .split('\n') to structure output.

Editable Question Boxes:

Questions appeared in text areas, making them editable.

Solution: Replaced with st.markdown() for readonly display.

API Rate Limits:

Hugging Face API had request limits.

Solution: Cached API responses where possible.

Data Privacy Concerns:

Candidate details needed protection.

Solution: Implemented Fernet encryption before storing data.

📜 License

This project is open-source under the MIT License.

👥 Contributors

Pavankumar T

💬 Have Feedback or Questions?

Feel free to open an issue or contribute to the repository!
