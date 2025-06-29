from transformers import pipeline
import os
from dotenv import load_dotenv

load_dotenv()

# Create Hugging Face pipelines
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

def generate_summary(raw_text):
    if len(raw_text) > 1024:
        raw_text = raw_text[:1024]
    result = summarizer(raw_text)
    return result[0]['summary_text']

def answer_question(raw_text, query):
    if len(raw_text) > 1024:
        raw_text = raw_text[:1024]
    result = qa_pipeline(question=query, context=raw_text)
    return result['answer']
