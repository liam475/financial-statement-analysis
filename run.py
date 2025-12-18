from __future__ import annotations

import pandas as pd

from data_loader import load_all
from normalizer import normalize_income, build_master
from metrics import add_metrics
from valuation import valuation_table
from exporter import export_to_excel

def _cagr(series: pd.Series) -> float:
    s = series.dropna()
    if len(s) < 2:
        return float("nan")
    start = float(s.iloc[0])
    end = float(s.iloc[-1])
    if start <= 0:
        return float("nan")
    periods = len(s) - 1  # annual rows assumed
    return (end / start) ** (1 / periods) - 1

def build_summary(master: pd.DataFrame, valuation: pd.DataFrame) -> pd.DataFrame:
    df = master.sort_values("date").copy()

    # Add summary stats (same value repeated each row so it's visible anywhere)
    df["revenue_cagr"] = _cagr(df["revenue"])
    df["ebitda_margin_change_pp"] = (df["ebitda_margin"].iloc[-1] - df["ebitda_margin"].iloc[0]) * 100

    # Bring in valuation multiples (latest row only)
    val = valuation.copy()
    val["date"] = pd.to_datetime(val["date"])
    df = df.merge(val[["date", "enterprise_value", "EV/Revenue", "EV/EBITDA"]], on="date", how="left")

    # Scale to $mm for IB-style readability
    money_cols = ["revenue", "ebitda_normalized", "fcf", "net_debt", "enterprise_value"]
    for c in money_cols:
        df[c] = df[c] / 1_000_000

    # Build clean output columns
    summary = df[
        [
            "date",
            "revenue",
            "revenue_yoy",
            "revenue_cagr",
            "ebitda_normalized",
            "ebitda_margin",
            "ebitda_margin_change_pp",
            "fcf",
            "net_debt",
            "enterprise_value",
            "EV/Revenue",
            "EV/EBITDA",
            "roic",
        ]
    ].copy()

    # Clean rounding (like Excel outputs in banking)
    summary["revenue"] = summary["revenue"].round(1)
    summary["ebitda_normalized"] = summary["ebitda_normalized"].round(1)
    summary["fcf"] = summary["fcf"].round(1)
    summary["net_debt"] = summary["net_debt"].round(1)
    summary["enterprise_value"] = summary["enterprise_value"].round(1)

    summary["EV/Revenue"] = summary["EV/Revenue"].round(2)
    summary["EV/EBITDA"] = summary["EV/EBITDA"].round(2)

    summary["revenue_yoy"] = summary["revenue_yoy"].round(4)
    summary["revenue_cagr"] = summary["revenue_cagr"].round(4)
    summary["ebitda_margin"] = summary["ebitda_margin"].round(4)
    summary["roic"] = summary["roic"].round(4)

    # EBITDA margin change in percentage points (already in pp), keep 1 decimal
    summary["ebitda_margin_change_pp"] = summary["ebitda_margin_change_pp"].round(1)
    # Pretty, presentation-ready column names for Summary tab
    summary = summary.rename(
        columns={
            "date": "Date",
            "revenue": "Revenue ($mm)",
            "revenue_yoy": "Revenue YoY (%)",
            "revenue_cagr": "Revenue CAGR (%)",
            "ebitda_normalized": "EBITDA (Normalized) ($mm)",
            "ebitda_margin": "EBITDA Margin (%)",
            "ebitda_margin_change_pp": "EBITDA Margin Δ (pp)",
            "fcf": "Free Cash Flow ($mm)",
            "net_debt": "Net Debt ($mm)",
            "enterprise_value": "Enterprise Value ($mm)",
            "EV/Revenue": "EV / Revenue (x)",
            "EV/EBITDA": "EV / EBITDA (x)",
            "roic": "ROIC (%)",
        }
    )
    summary = summary.tail(1).reset_index(drop=True)

    return summary

def main() -> None:
    inc, bal, cf = load_all("data")
    inc_n = normalize_income(inc)
    master = build_master(inc_n, bal, cf)
    master = add_metrics(master)

    market_cap = 2500.0
    val = valuation_table(master, market_cap=market_cap)

    summary = build_summary(master, val)

    export_to_excel(master, val, summary, "outputs/valuation_output.xlsx")
    print("Done ✅ Wrote outputs/valuation_output.xlsx")

if __name__ == "__main__":
    main()
