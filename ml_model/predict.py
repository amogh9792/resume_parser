import joblib

def predict_resume_relevance(text):
    """Predict relevance of a resume using trained ML model."""
    classifier = joblib.load("models/resume_classifier.pkl")
    vectorizer = joblib.load("models/tfidf_vectorizer.pkl")
    text_vectorized = vectorizer.transform([text])
    return classifier.predict(text_vectorized)[0]
