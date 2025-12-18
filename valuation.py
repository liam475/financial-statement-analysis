from __future__ import annotations
import pandas as pd

def valuation_table(df: pd.DataFrame, market_cap: float) -> pd.DataFrame:
    latest = df.sort_values("date").iloc[-1].copy()

    enterprise_value = market_cap + latest["total_debt"] - latest["cash"]

    out = pd.DataFrame(
        {
            "date": [latest["date"].date()],
            "market_cap": [market_cap],
            "enterprise_value": [enterprise_value],
            "revenue": [latest["revenue"]],
            "ebitda_normalized": [latest["ebitda_normalized"]],
            "net_debt": [latest["net_debt"]],
            "EV/Revenue": [enterprise_value / latest["revenue"]],
            "EV/EBITDA": [enterprise_value / latest["ebitda_normalized"]],
        }
    )
    return out
