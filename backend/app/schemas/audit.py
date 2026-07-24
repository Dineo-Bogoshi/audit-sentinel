from pydantic import BaseModel
from typing import List, Dict, Any

class AuditSummaryResponse(BaseModel):
    filename: str
    total_records_processed: int
    total_exceptions_found: int
    exception_summary: List[Dict[str, Any]]