from __future__ import annotations
import pandas as pd

def normalize_income(inc: pd.DataFrame) -> pd.DataFrame:
    inc = inc.copy()

    inc["gross_profit"] = inc["revenue"] - inc["cogs"]
    inc["gross_margin"] = inc["gross_profit"] / inc["revenue"]

    inc["ebit_pre_ones"] = inc["gross_profit"] - inc["sg&a"] - inc["d&a"]
    inc["ebit_normalized"] = inc["ebit_pre_ones"] - inc["one_time_items"]
    inc["ebitda_normalized"] = inc["ebit_normalized"] + inc["d&a"]
    inc["ebitda_margin"] = inc["ebitda_normalized"] / inc["revenue"]

    return inc

def build_master(inc: pd.DataFrame, bal: pd.DataFrame, cf: pd.DataFrame) -> pd.DataFrame:
    df = inc.merge(bal, on="date", how="outer").merge(cf, on="date", how="outer")
    df = df.sort_values("date").reset_index(drop=True)
    return df
