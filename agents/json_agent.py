# agents/json_agent.py

import json

# Define a simple target schema (keys expected)
TARGET_SCHEMA = {
    "id": str,
    "customer": str,
    "items": list,
    "total": float
}

def validate_and_reformat(json_data):
    missing_fields = []
    extra_fields = []
    reformatted = {}

    for key in TARGET_SCHEMA:
        if key not in json_data:
            missing_fields.append(key)
        else:
            reformatted[key] = json_data[key]

    for key in json_data:
        if key not in TARGET_SCHEMA:
            extra_fields.append(key)

    return {
        "cleaned_data": reformatted,
        "missing_fields": missing_fields,
        "extra_fields": extra_fields
    }
