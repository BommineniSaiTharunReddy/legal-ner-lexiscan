# 🧾 LexiScan Auto – Intelligent Legal Entity Extraction (NER)

An end-to-end NLP pipeline for automated extraction of key entities from unstructured legal contracts using OCR and Custom Named Entity Recognition (NER).

---

##  Project Overview

LexiScan Auto is designed to process high-volume unstructured legal PDF contracts and extract structured information such as:

-  Effective Dates  
-  Party Names  
-  Monetary Values  
-  Jurisdiction  

Traditional Regex-based extraction is rigid and error-prone.  
This project implements a contextual deep learning-based NER system tailored specifically for legal documents.

---

##  System Architecture

Scanned PDF  
↓  
Tesseract OCR  
↓  
Clean Extracted Text  
↓  
Custom SpaCy NER Model  
↓  
Structured JSON Output  
↓  
Validation & Heuristic Checks  

---

##  Tech Stack

- Python  
- SpaCy (Custom NER Training)  
- TensorFlow / Bi-LSTM (experimental deep learning model)  
- Tesseract OCR  
- pdf2image  
- JSON-based structured output  

---

##  Project Structure

legal-ner-lexiscan/  
│  
├── src/  
│   ├── ocr.py              # OCR processing  
│   ├── train_ner.py        # Model training script  
│   ├── evaluate.py         # Model evaluation  
│   └── main.py             # Inference pipeline  
│  
├── data/                   # Sample / synthetic contracts  
├── models/                 # Saved trained model (ignored in Git)  
├── requirements.txt  
└── README.md  

---

##  Installation

### 1️⃣ Clone Repository

git clone https://github.com/BommineniSaiTharunReddy/legal-ner-lexiscan.git  
cd legal-ner-lexiscan  

### 2️⃣ Create Virtual Environment

python -m venv venv  
venv\Scripts\activate  

### 3️⃣ Install Dependencies

pip install -r requirements.txt  

---

##  Training the NER Model

python src/train_ner.py  

This will:
- Train a custom legal-domain NER model  
- Save the trained model inside the `models/` directory  

---

##  Running Entity Extraction

python src/main.py  

### Sample Output

{
  "Extracted_Entities": {
    "DATE": ["March 10, 2026"],
    "PARTY": ["Alpha Tech Solutions Pvt Ltd"],
    "MONEY": ["$1,200,000"],
    "JURISDICTION": ["Texas, USA"]
  },
  "Validation_Checks": {
    "Date_Sequence_Valid": true,
    "Valid_Monetary_Values": true
  }
}

---

##  Model Evaluation

python src/evaluate.py  

Evaluation includes:
- Precision  
- Recall  
- F1 Score  
- Testing on held-out legal-style contract text  

---

##  Key Features

✔ End-to-end OCR + NLP pipeline  
✔ Custom domain-specific NER model  
✔ Structured JSON output  
✔ Validation and heuristic logic  
✔ Production-oriented project structure  

---

##  Future Enhancements

- Fine-tune BERT-based legal transformer model  
- Deploy using FastAPI REST API  
- Docker containerization  
- CI/CD integration  
- Cloud deployment (AWS / Azure)  

---

##  License

This project is developed for educational and research purposes.