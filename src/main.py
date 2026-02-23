from ocr import extract_text_from_pdf
import spacy
from collections import defaultdict
from datetime import datetime
import re
import json

# -------------------------
# Helper: Parse Date Safely
# -------------------------
def parse_date(date_string):
    try:
        return datetime.strptime(date_string, "%B %d, %Y")
    except:
        return None


# -------------------------
# Main Execution
# -------------------------
if __name__ == "__main__":

    pdf_path = "data/raw_pdfs/sample.pdf"

    nlp = spacy.load("models/legal_ner_model")
    text = extract_text_from_pdf(pdf_path)
    doc = nlp(text)

    result = defaultdict(list)

    for ent in doc.ents:
        if ent.text not in result[ent.label_]:
            result[ent.label_].append(ent.text)

    # -------------------------
    # Validation Layer
    # -------------------------

    validation = {}

    # Date validation
    if "DATE" in result and len(result["DATE"]) >= 2:
        parsed_dates = [parse_date(d) for d in result["DATE"] if parse_date(d)]
        parsed_dates.sort()

        if len(parsed_dates) >= 2:
            if parsed_dates[0] < parsed_dates[-1]:
                validation["Date_Sequence_Valid"] = True
            else:
                validation["Date_Sequence_Valid"] = False

    # Money validation (must contain currency symbol)
    if "MONEY" in result:
        valid_money = []
        for money in result["MONEY"]:
            if re.search(r"[$€£]", money):
                valid_money.append(money)

        validation["Valid_Monetary_Values"] = valid_money

    # -------------------------
    # Final Output
    # -------------------------

    final_output = {
        "Extracted_Entities": result,
        "Validation_Checks": validation
    }

    print("\n------ FINAL STRUCTURED OUTPUT ------\n")
    print(json.dumps(final_output, indent=4))