import pandas as pd

class PIIProtector:
    @staticmethod
    def mask_email(email: str) -> str:
        if not isinstance(email, str) or "@" not in email:
            return email
        name, domain = email.split("@", 1)
        masked_name = name[0] + "***" if len(name) > 1 else "*"
        return f"{masked_name}@{domain}"

    @staticmethod
    def mask_id_or_account(val: str) -> str:
        val_str = str(val)
        if len(val_str) > 4:
            return "*" * (len(val_str) - 4) + val_str[-4:]
        return val_str

    def sanitize_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        clean_df = df.copy()
        for col in clean_df.columns:
            col_lower = col.lower()
            if "email" in col_lower:
                clean_df[col] = clean_df[col].apply(self.mask_email)
            elif any(k in col_lower for k in ["id", "account", "card"]):
                clean_df[col] = clean_df[col].apply(self.mask_id_or_account)
        return clean_df