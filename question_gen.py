from transformers import pipeline

# ✅ Open, free model for text generation (question generation)
question_gen_pipeline = pipeline("text-generation", model="tiiuae/falcon-rw-1b", max_new_tokens=100)
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

def generate_logic_questions(text):
    prompt = f"""Generate 3 logic-based or comprehension questions from this document:\n{text[:500]}"""
    result = question_gen_pipeline(prompt)
    return result[0]['generated_text'].split("\\n")[-3:]  # Return last 3 lines

def evaluate_user_response(question, user_answer, context):
    if len(context) > 1024:
        context = context[:1024]
    feedback = qa_pipeline(question=question, context=context)
    answer = feedback['answer']

    if user_answer.strip().lower() in answer.strip().lower():
        return f"✅ Correct! Based on the document, the correct answer is: {answer}"
    else:
        return f"❌ Not quite. A better answer would be: {answer}"
