# TalentScout Hiring Assistant Chatbot

## Project Overview:
The **Hiring Assistant Chatbot** is an AI-powered tool designed to streamline the initial screening process for technical job applicants whether thay are freshers or experienced. It helps recruiters gather candidate details, generate relevant technical interview questions, and conduct real-time chatbot-based conversations. The chatbot is powered by Google's **Gemini AI** and provides a structured & interactive experience for candidates throughout the screening process.

## 🛠Installation Instructions:
Follow these steps to set up and run the application locally:

### 1️. **Clone the Repository**
```bash
git clone https://github.com/your-repo/hiring-assistant-chatbot.git
cd hiring-assistant-chatbot
```

### 2. **Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```

### 3️. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️. **Set Up API Keys**
- Create a `.env` file in the project root and add the following:
  ```env
  GEMINI_API_KEY=your_google_gemini_api_key
  ```
- Replace `your_google_gemini_api_key` with your actual API key.

### 5️. **Run the Application**
```bash
streamlit run app.py
```
This will start a local Streamlit server, and the chatbot will be accessible via web browser.

## Usage Guide:
1️⃣ Open the Streamlit app in your browser.
2️⃣ Enter your personal details (Name, Email, Experience, Tech Stack, etc.).
3️⃣ Click **"Generate Questions"** to receive 3-5 technical interview questions based on your tech stack.
4️⃣ Answer the questions and submit them for review.
5️⃣ Interact with the AI chatbot in real-time for any additional inquiries.

## Technical Details:
- **Frontend & UI**: Built using **Streamlit** for an interactive and user-friendly experience.
- **AI Model**: Utilizes **Google Gemini AI** (`gemini-pro`) for NLP-based responses.
- **Data Processing**: User inputs are sanitized and structured for accurate responses.
- **Backend**: Pure Python with a minimalistic approach to ensure smooth execution.
- **Privacy**: Used cryptography to secure the candidates details.

### Libraries Used:
- `streamlit` → UI framework
- `google-generativeai` → API wrapper for Gemini AI
- `cryptography` → Security and Privacy

## Prompt Design:
The chatbot uses carefully structured prompts to ensure precise and engaging interactions:
1️. **Technical Question Generation**:
   ```text
   Generates exactly 3 to 5 concise technical interview questions based on the candidate tech stack.
   Ensure the response is a numbered list with one question per line. Keep questions short and relevant.
   ```
2️. **Chatbot Responses**:
   ```text
   Act as an AI interview assistant. Respond concisely to: {user_input}.
   ```
   - Ensures the chatbot remains on-topic and professional.
   - Allows for open-ended yet structured responses.

## Challenges & Solutions:
### **Challenge: Generating high-quality technical questions**
**Solution:** Iteratively refined the prompt to enforce concise, numbered responses and prevent generic questions.

### **Challenge: Maintaining real-time chat behavior in Streamlit**
**Solution:** Used `st.session_state` to persist chat history and dynamically update messages without page refresh.

### **Challenge: Ensuring user-friendly UI and clear interactions**
**Solution:** Implemented visually distinct chat bubbles, structured form inputs, and logical question-answer flows.

## Future Enhancements:
-  Add integration with ATS (Applicant Tracking Systems)
-  Implement audio-based Q&A for verbal technical interviews
-  Implement coding type technical questions.

contributed by,
Pavankumar T

**📢 Developed with ❤️ to simplify hiring and enhance candidate experience! 🚀**
