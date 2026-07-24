import os
import hashlib
import requests
import streamlit as st

API_URL = os.environ.get("AUDIT_API_URL", "http://127.0.0.1:8000/audit/process-csv")

def calculate_file_hash(file_bytes: bytes) -> str:
    return hashlib.md5(file_bytes).hexdigest()

@st.cache_data(show_spinner=False)
def execute_audit_scan(file_bytes: bytes, filename: str, file_hash: str) -> dict:
    files = {"file": (filename, file_bytes, "text/csv")}
    response = requests.post(API_URL, files=files, timeout=60)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise RuntimeError(f"API Error ({response.status_code}): {response.text}")