Here is a **README.md** file for your AI Resume Parser project.

---

# **📄 AI Resume Parser with Machine Learning**

🚀 **An AI-powered Resume Parser that extracts skills, contact details, and ranks resumes based on job descriptions using NLP and Machine Learning.**

---

## **📌 Features**

✅ **Extracts Email & Phone Numbers** from resumes  
✅ **Detects Skills** using NLP  
✅ **Matches Resume with Job Descriptions** using AI  
✅ **Ranks Resumes as Relevant/Not Relevant** using ML  
✅ **Exports Results to CSV**  
✅ **Simple GUI for easy use**

---

## **🛠️ Setup & Installation**

### **1️⃣ Install Dependencies**

Ensure you have Python **3.8+**, then run:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, create it with:

```
spacy
pdfplumber
fuzzywuzzy
python-Levenshtein
numpy
scikit-learn
joblib
pandas
tk
```

### **2️⃣ Download NLP Model for Spacy**

```bash
python -m spacy download en_core_web_sm
```

### **3️⃣ Train the Machine Learning Model**

Before running the app, train the model:

```bash
python ml_model/train_model.py
```

✅ This creates:

- `models/resume_classifier.pkl` → Trained ML model
- `models/tfidf_vectorizer.pkl` → TF-IDF vectorizer

---

## **🚀 Running the AI Resume Parser**

### **1️⃣ Start the GUI**

```bash
python main.py
```

### **2️⃣ Upload Resume & Get Insights**

- Enter a **job description**
- Click **Upload Resume** (select a PDF)
- See **parsed results** instantly

### **3️⃣ View Exported Resumes**

Parsed resumes are stored in **`parsed_resumes.csv`**.

---

## **📂 Project Structure**

```
resume_parser_project/
│── main.py                # Entry point (Runs GUI & ML model)
│── parser/
│   │── text_extraction.py # Extract text from PDF
│   │── contact_info.py    # Extract email, phone
│   │── skills_extraction.py # Extract skills
│   │── job_matching.py    # Match resume to job
│── ml_model/
│   │── train_model.py     # Trains ML model
│   │── predict.py         # Predicts resume relevance
│── gui/
│   │── app.py             # GUI using Tkinter
│── utils/
│   │── export_csv.py      # Saves parsed data to CSV
│── models/
│   │── resume_classifier.pkl  # Trained model
│   │── tfidf_vectorizer.pkl   # TF-IDF vectorizer
│── data/
│   │── sample_resumes/    # Folder for test resumes
│── requirements.txt       # Dependencies
│── README.md              # Documentation
```

---

## **🎯 Future Enhancements**

- **📊 Add a Dashboard** (Top Skills, Best Candidates)
- **🕵️ Detect Fake Resumes** (Keyword stuffing detection)
- **🌐 Web Version** (Using Streamlit/Flask)
