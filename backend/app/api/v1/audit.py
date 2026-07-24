from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
import pandas as pd
from app.services.privacy import PIIProtector
from app.services.anomaly_engine import AuditAnomalyEngine
from app.schemas.audit import AuditSummaryResponse

router = APIRouter(prefix="/audit", tags=["Audit Engine"])

def get_pii_protector() -> PIIProtector:
    return PIIProtector()

def get_anomaly_engine() -> AuditAnomalyEngine:
    return AuditAnomalyEngine()

# Standard 'def' allows FastAPI to handle CPU-bound pandas computations in worker threads
@router.post("/process-csv", response_model=AuditSummaryResponse)
def process_audit_file(
    file: UploadFile = File(...),
    pii_protector: PIIProtector = Depends(get_pii_protector),
    anomaly_engine: AuditAnomalyEngine = Depends(get_anomaly_engine),
):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Please upload a CSV file.")
    
    try:
        # Stream file buffer directly into pandas
        df = pd.read_csv(file.file)
        
        sanitized_df = pii_protector.sanitize_dataframe(df)
        audited_df = anomaly_engine.analyze_transactions(sanitized_df)
        flagged = audited_df[audited_df["is_flagged"]]
        
        return AuditSummaryResponse(
            filename=file.filename,
            total_records_processed=len(audited_df),
            total_exceptions_found=len(flagged),
            exception_summary=flagged.to_dict(orient="records")
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process CSV file: {str(e)}")