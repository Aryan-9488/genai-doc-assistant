# 📚 GenAI-Powered Research Assistant

This project is a smart assistant that reads structured documents (like PDFs), generates summaries, answers questions, and quizzes users — using entirely free and open-source Hugging Face models.

---

## 🚀 Features

- 📄 Upload and parse PDFs
- 🧾 Auto Summarization (≤150 words)
- 💬 Ask Anything Mode (QA from doc)
- 🧠 Challenge Me Mode (auto quiz + evaluation)
- 🔍 100% Free: Uses Hugging Face models (no OpenAI required)

---

## 🧰 Tech Stack

- `Streamlit` (Frontend)
- `transformers`, `pdfplumber`, `dotenv`
- Models used:
  - `distilbart-cnn-12-6` (summarization)
  - `distilbert-base-uncased-distilled-squad` (QA)
  - `falcon-rw-1b` (question generation)

---

## 🔧 Setup Instructions

```bash
git clone https://github.com/<your-username>/genai-doc-assistant.git
cd genai-doc-assistant

# Create and activate virtual environment
python -m venv venv
venv\\Scripts\\activate    # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app/main.py
