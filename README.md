# Audit Sentinel

**Audit Sentinel** is an automated financial auditing and compliance web application. It combines a **FastAPI** backend featuring automated PII sanitization and machine-learning-based anomaly detection with a modern **Streamlit** frontend dashboard.

---

## Architecture Overview

The repository is structured as a decoupled monorepo separating business logic and machine learning pipelines from the presentation layer:

```text
fin-sentinel/
├── backend/                  # FastAPI REST Service
│   ├── app/
│   │   ├── api/v1/          # Route handlers & endpoints
│   │   ├── schemas/         # Pydantic data validation
│   │   └── services/        # PII redaction & Isolation Forest engine
│   ├── run.py               # Uvicorn entrypoint
│   └── requirements.txt
│
├── frontend/                 # Streamlit UI Dashboard
│   ├── assets/              # UI logos and graphics
│   ├── components/          # Reusable UI widgets & state handlers
│   ├── services/            # API client & caching
│   ├── styles/              # High-contrast CSS theme system
│   ├── streamlit_app.py     # Main application dashboard
│   └── requirements.txt
│
├── scripts/                  # Data generators & CLI utils
│   └── generate_data.py
│
├── sample_data/              # Generated mock ledgers
└── README.md
```

## Features

* **Automated PII Masking:** Sanitizes sensitive inputs (emails, account numbers, personal identifiers) prior to analytical processing.
* **Machine Learning Auditing:** Employs an IsolationForest engine to flag statistical outliers, duplicate entries, and governance rule violations in financial ledgers.
* **Cached API Integration:** MD5 checksum verification prevents redundant server requests and optimizes Streamlit reruns.
* **Exportable Exception Reports:** Interactive visualization grids with quick-download options for compliance logging.

## Quick Start Guide

<details>
<summary><b>Click to expand Installation & Setup Instructions</b></summary>

### 1. Prerequisites & Environment Setup

```bash
# Clone repository
git clone https://github.com/Dineo-Bogoshi/audit-sentinel.git
cd audit-sentinel

# Create and activate virtual environment
python -m venv venv

# macOS / Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate

# Install all dependencies
pip install -r backend/requirements.txt -r frontend/requirements.txt
```

### 2. Generate Sample Ledger Data

Populate the `sample_data/` folder with mock financial CSV records:

```bash
python scripts/generate_data.py
```

### 3. Run the Application

Launch both services in split terminal windows (with your virtual environment activated in both):

**Terminal 1: Backend (FastAPI)**
```bash
cd backend
python run.py
```
* Server runs on http://127.0.0.1:8000
* Interactive OpenAPI documentation available at http://127.0.0.1:8000/docs

**Terminal 2: Frontend (Streamlit)**
```bash
cd frontend
streamlit run streamlit_app.py
```
* Dashboard automatically launches at http://localhost:8501

</details>

## Tech Stack

* **Backend:** Python, FastAPI, Uvicorn, Pydantic, Scikit-Learn, Pandas
* **Frontend:** Streamlit, Plotly, Requests
* **Data & Testing:** Synthetic ledger generators, Isolation Forest, Regex PII redact pipelines
