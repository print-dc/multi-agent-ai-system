

import re
from agents.classifier_agent import classify_input

def extract_sender(text):
    # Naive extraction using regex
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else "Unknown"

def detect_urgency(text):
    if any(word in text.lower() for word in ["urgent", "asap", "immediately", "high priority"]):
        return "High"
    elif any(word in text.lower() for word in ["soon", "priority"]):
        return "Medium"
    else:
        return "Low"

def process_email(email_text):
    sender = extract_sender(email_text)
    urgency = detect_urgency(email_text)
    classification = classify_input(email_text)  # Reuse our classifier

    return {
        "sender": sender,
        "urgency": urgency,
        "intent": classification["intent"],
        "format": classification["format"],
        "summary": email_text[:100] + "..." if len(email_text) > 100 else email_text
    }
