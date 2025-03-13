from fuzzywuzzy import fuzz

def match_resume_to_job(resume_text, job_text):
    """Match resume to job description using text similarity."""
    return fuzz.token_set_ratio(resume_text, job_text)
