import pandas as pd
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os

if not os.path.exists("models"):
    os.makedirs("models")

def load_resume_data():
    """Load resumes and labels from dataset (Kaggle CSV file)."""
    df = pd.read_csv("data/resume_data.csv")  
    resumes = df["Resume"].values  
    labels = df["Category"].factorize()[0] 
    return resumes, labels

def train_ml_model():
    """Train and save an ML model for resume ranking."""
    print("📥 Loading resume data...")
    resumes, labels = load_resume_data()

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(resumes)
    y = np.array(labels)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    classifier = RandomForestClassifier(n_estimators=50, random_state=42)
    classifier.fit(X_train, y_train)

    # Save Model & Vectorizer
    joblib.dump(classifier, "models/resume_classifier.pkl")
    joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")

    print(f"✅ Model trained with accuracy: {accuracy_score(y_test, classifier.predict(X_test)) * 100:.2f}%")

if __name__ == "__main__":
    train_ml_model()
