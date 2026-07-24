# Autonomous Natural Language to SQL Engine

An end-to-end, agentic **Natural Language to SQL Engine** built with **FastAPI**, **LangChain**, **Groq (Llama 3.3 70B)**, and **Streamlit**.

This application allows non-technical users to query database tables using plain English questions. The underlying autonomous agent dynamically discovers the database schema, drafts SQL queries, validates them for syntax correctness, executes them safely against SQLite (or PostgreSQL), and presents the summarized results in a clean chat interface.

---

## 🌟 Key Features

* **Autonomous Schema Discovery:** Automatically inspects database tables, column names, relationships, and sample data.
* **Self-Healing SQL Generation:** Utilizes LangChain's `SQLDatabaseToolkit` with query checking and self-correction steps.
* **FastAPI Backend:** High-performance RESTful API powering the agent workflow.
* **Interactive Streamlit UI:** Modern, chat-based frontend interface for seamless user interaction.
* **Groq Acceleration:** Powered by `llama-3.3-70b-versatile` for rapid reasoning and query drafting.

---

## 🏗️ Architecture & Autonomous Workflow

The core agent follows a 5-step autonomous loop:

[ User Prompt ]
│
▼
[ Streamlit App UI ] ──( HTTP GET / POST )──► [ FastAPI Server ]
│
▼
┌──────────────────────────────────────────────────────────────┐
│                    LangChain Agent Loop                      │
│                                                              │
│  1. Table Discovery    ──► List tables in database           │
│  2. Schema Inspection  ──► Inspect columns, types & samples  │
│  3. Query Generation   ──► Draft appropriate SQL query       │
│  4. Query Checker      ──► Validate syntax before execution  │
│  5. Execution & Heal   ──► Execute query / catch & fix errors│
└──────────────────────────────────────────────────────────────┘
│
▼
[ SQLite Database ]

---

## 📁 Repository Structure

```text
.
├── main.py              # FastAPI application & LangChain Agent pipeline
├── app.py               # Streamlit chat interface
├── requirements.txt     # Python dependencies
├── .gitignore           # Git ignore rules
├── .env                 # Environment variables (API Keys)
├── ecommerce.db         # SQLite database file
└── README.md            # Project documentation