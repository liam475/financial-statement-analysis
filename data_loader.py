from __future__ import annotations
import pandas as pd
from pathlib import Path

def load_statement(path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    if "date" not in df.columns:
        raise ValueError(f"'date' column missing in {path}")
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").reset_index(drop=True)
    return df

def load_all(data_dir: str | Path) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    data_dir = Path(data_dir)
    inc = load_statement(data_dir / "income_statement.csv")
    bal = load_statement(data_dir / "balance_sheet.csv")
    cf = load_statement(data_dir / "cash_flow.csv")
    return inc, bal, cf
