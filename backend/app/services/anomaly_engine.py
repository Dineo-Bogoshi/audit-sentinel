import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

class AuditAnomalyEngine:
    def __init__(self, contamination: float = 0.05):
        self.model = IsolationForest(contamination=contamination, random_state=42)

    def analyze_transactions(self, df: pd.DataFrame) -> pd.DataFrame:
        results_df = df.copy()
        results_df["audit_flags"] = ""

        if "account_id" in results_df.columns and "amount" in results_df.columns:
            duplicates = results_df.duplicated(subset=["account_id", "amount"], keep=False)
            results_df.loc[duplicates, "audit_flags"] += "POTENTIAL_DUPLICATE; "

        numeric_cols = results_df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            features = results_df[numeric_cols].fillna(0)
            predictions = self.model.fit_predict(features)
            is_anomaly = predictions == -1
            results_df.loc[is_anomaly, "audit_flags"] += "STATISTICAL_ANOMALY; "

        results_df["audit_flags"] = results_df["audit_flags"].str.rstrip("; ")
        results_df["is_flagged"] = results_df["audit_flags"] != ""
        return results_df