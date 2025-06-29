import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.pdf_utils import extract_text_from_pdf
from utils.qa_utils import generate_summary, answer_question
from utils.question_gen import generate_logic_questions, evaluate_user_response


st.set_page_config(page_title="GenAI Research Assistant", layout="wide")
st.title("📚 GenAI-Powered Research Assistant")

uploaded_file = st.file_uploader("📄 Upload your research/report document (PDF only)", type=["pdf"])

if uploaded_file:
    raw_text = extract_text_from_pdf(uploaded_file)
    if not raw_text:
        st.error("❌ Unable to extract text from the PDF. Please check the file format or content.")
        st.stop()

    st.subheader("🧾 Auto Summary")
    summary = generate_summary(raw_text)
    st.success(summary)

    mode = st.radio("Select a mode:", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        user_question = st.text_input("🔍 Ask a question from the document:")
        if user_question:
            answer = answer_question(raw_text, user_question)
            st.markdown("#### 💬 Answer")
            st.info(answer)

    elif mode == "Challenge Me":
        if st.button("🧠 Generate Questions"):
            questions = generate_logic_questions(raw_text)
            st.session_state.questions = questions.split('\n')

        if "questions" in st.session_state:
            for i, q in enumerate(st.session_state.questions):
                if q.strip() == "":
                    continue
                st.markdown(f"**Q{i+1}: {q.strip()}**")
                user_input = st.text_input(f"Your answer {i+1}", key=f"answer_{i}")
                if user_input:
                    feedback = evaluate_user_response(q, user_input, raw_text)
                    st.markdown("**📝 Feedback:**")
                    st.warning(feedback)
