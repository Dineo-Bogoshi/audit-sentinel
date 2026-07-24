from fastapi import FastAPI
from app.api.v1.audit import router as audit_router

app = FastAPI(title="Audit Sentinel API", version="1.0.0")

app.include_router(audit_router)

@app.get("/")
def root():
    return {"status": "active", "system": "Audit Sentinel API"}