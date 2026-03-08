import spacy
import os
from src.ocr import extract_text_from_pdf
from src.post_processing import clean_entities

nlp = spacy.load("models/legal_ner_model")


def extract_entities_from_pdf(pdf_path):

    # convert to absolute path (fix for pytest)
    pdf_path = os.path.abspath(pdf_path)

    text = extract_text_from_pdf(pdf_path)

    doc = nlp(text)

    entities = clean_entities(doc)

    return entities