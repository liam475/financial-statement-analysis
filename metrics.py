from __future__ import annotations
import pandas as pd

def add_metrics(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["revenue_yoy"] = df["revenue"].pct_change()
    df["fcf"] = df["cfo"] + df["capex"]
    df["net_debt"] = df["total_debt"] - df["cash"]

    df["nwc"] = (df["accounts_receivable"] + df["inventory"]) - df["accounts_payable"]
    df["nwc_change"] = df["nwc"].diff()

    denom = df["ebit_pre_ones"].abs().clip(lower=1e-9)
    tax_rate = (df["taxes"] / denom).clip(0, 0.5)
    df["nopat"] = df["ebit_normalized"] * (1 - tax_rate)

    df["invested_capital"] = df["nwc"] + df["pp&e"]
    df["roic"] = df["nopat"] / df["invested_capital"]

    return df
