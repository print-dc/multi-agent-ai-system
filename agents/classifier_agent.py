# agents/classifier_agent.py

import json

def classify_input(input_text):
    input_text = input_text.strip().lower()

    # Format Detection
    if input_text.startswith("{") and input_text.endswith("}"):
        detected_format = "JSON"
    elif "subject:" in input_text or "dear" in input_text:
        detected_format = "Email"
    elif "pdf" in input_text or "%PDF" in input_text:
        detected_format = "PDF"
    else:
        detected_format = "Unknown"

    # Intent Detection (rule-based for now)
    if "invoice" in input_text:
        intent = "Invoice"
    elif "quote" in input_text or "rfq" in input_text:
        intent = "RFQ"
    elif "complaint" in input_text or "issue" in input_text:
        intent = "Complaint"
    elif "regulation" in input_text or "compliance" in input_text:
        intent = "Regulation"
    else:
        intent = "Other"

    return {
        "format": detected_format,
        "intent": intent
    }
