# 🧠 Multi-Agent AI System

This project is a lightweight, modular multi-agent AI system that accepts inputs in various formats (PDF, JSON, or Email), detects format and intent, and routes the data to specialized agents for processing — all while maintaining a shared memory for traceability.

---

## 🚀 Features

- **Format Detection**: Identifies if input is Email, JSON, or PDF.
- **Intent Classification**: Detects the purpose (e.g., RFQ, Complaint, Invoice, etc.).
- **Agent Routing**:
  - **Email Agent**: Extracts sender, urgency, and summary.
  - **JSON Agent**: Parses structured JSON and flags missing fields.
- **Shared Memory Module**: Stores format, timestamp, extracted data, and thread context using SQLite.

---

## 🧱 Architecture

User Input (PDF / Email / JSON)
↓
Classifier Agent → Determines Format + Intent
↓
Routes to Appropriate Agent (Email Agent / JSON Agent)
↓
Extracted info logged in Shared Memory


---

## 📂 Folder Structure

multi_agent_system/
│
├── agents/
│ ├── init.py
│ ├── classifier_agent.py
│ ├── email_agent.py
│ └── json_agent.py
│
├── memory/
│ └── shared_memory.py
│
├── utils.py
├── main.py
└── README.md


---

## 🧪 Example Use Case

- A user sends an email requesting a quote.
- Classifier detects it's an Email + RFQ.
- Routes to Email Agent.
- Info is extracted (e.g., sender, urgency).
- Shared memory logs the result with timestamp and source.

---

## 🛠️ Tech Stack

- Python
- OpenAI / LLM APIs (for intent detection)
- SQLite (Shared Memory)
- Modular Agent Architecture

---

## 📦 Setup & Run

```bash
# Clone the repository
git clone https://github.com/print-dc/multi-agent-ai-system.git
cd multi-agent-ai-system

# Run the main script
python main.py

---

## 🧪 Example Use Case

- A user sends an email requesting a quote.
- Classifier detects it's an Email + RFQ.
- Routes to Email Agent.
- Info is extracted (e.g., sender, urgency).
- Shared memory logs the result with timestamp and source.

---

## 🛠️ Tech Stack

- Python
- OpenAI / LLM APIs (for intent detection)
- SQLite (Shared Memory)
- Modular Agent Architecture

---

## 📦 Setup & Run

```bash
# Clone the repository
git clone https://github.com/print-dc/multi-agent-ai-system.git
cd multi-agent-ai-system

# Run the main script
python main.py
