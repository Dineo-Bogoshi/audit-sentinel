import pandas as pd
import numpy as np
import random
import os

def generate_mock_ledger(num_records: int = 1000) -> pd.DataFrame:
    np.random.seed(42)
    random.seed(42)

    account_ids = [f"ACC-{random.randint(10000, 99999)}" for _ in range(50)]
    emails = [f"user_{i}@example.com" for i in range(30)]

    data = {
        "transaction_id": [f"TXN-{100000 + i}" for i in range(num_records)],
        "account_id": [random.choice(account_ids) for _ in range(num_records)],
        "email": [random.choice(emails) for _ in range(num_records)],
        "amount": np.round(np.random.exponential(scale=250, size=num_records), 2),
        "department_code": np.random.choice(["FIN", "HR", "IT", "OPS", "MKT"], size=num_records),
    }

    df = pd.DataFrame(data)

    # Inject some deliberate anomalies for the engine to flag
    # 1. Duplicates
    df.loc[10, ["account_id", "amount"]] = df.loc[9, ["account_id", "amount"]]
    df.loc[25, ["account_id", "amount"]] = df.loc[24, ["account_id", "amount"]]

    # 2. High amount statistical outliers
    df.loc[50, "amount"] = 85000.00
    df.loc[150, "amount"] = 120000.00

    return df

if __name__ == "__main__":
    os.makedirs("sample_data", exist_ok=True)
    df = generate_mock_ledger(num_records=500)
    
    output_path = "sample_data/mock_financial_ledger.csv"
    df.to_csv(output_path, index=False)
    print(f"Sample data generated: {output_path} ({len(df)} records)")