# main.py

from agents.email_agent import process_email
from memory.shared_memory import log_entry, get_all_entries

if __name__ == "__main__":
    sample_email = """
    Subject: URGENT RFQ - 500 units of Product X

    Dear Sales Team,

    We need a quote for 500 units of Product X. Please send it ASAP.

    Regards,
    purchase.manager@clientcorp.com
    """

    processed = process_email(sample_email)
    print("Email Agent Output:")
    for key, value in processed.items():
        print(f"{key}: {value}")

    # 🔄 Log to shared memory
    log_entry(source="email_001", data_type="Email", extracted_data=processed)

    print("\nShared Memory Entries:")
    for entry in get_all_entries():
        print(entry)
