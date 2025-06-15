# memory/shared_memory.py

import datetime

# Simple in-memory memory store
shared_store = []

def log_entry(source, data_type, extracted_data):
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "source": source,
        "type": data_type,
        "data": extracted_data
    }
    shared_store.append(entry)
    return entry

def get_all_entries():
    return shared_store