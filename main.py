from parser.text_extraction import extract_text_from_pdf
from parser.contact_info import extract_contact_details
from parser.skills_extraction import extract_skills
from parser.job_matching import match_resume_to_job
from ml_model.train_model import train_ml_model
from ml_model.predict import predict_resume_relevance
from gui.app import start_gui
import json
import os
from utils.export_csv import export_to_csv

if not os.path.exists("models/resume_classifier.pkl"):
    train_ml_model()

def parse_resume(pdf_path, job_description):
    """Parse resume and return structured data."""
    text = extract_text_from_pdf(pdf_path)
    email, phone = extract_contact_details(text)
    skills = extract_skills(text)
    match_score = match_resume_to_job(text, job_description)
    relevance = predict_resume_relevance(text)

    result = {
        "Email": email,
        "Phone": phone,
        "Skills": skills,
        "Match Score": match_score,
        "AI Relevance Score": "Relevant" if relevance == 1 else "Not Relevant"
    }

    export_to_csv(result)
    return json.dumps(result, indent=4)

if __name__ == "__main__":
    start_gui(parse_resume)
