# Financial Statement Normalization and Valuation Engine

**Python | pandas | Financial Modeling | Valuation | Excel Automation**

A programmatic financial analysis engine that converts raw financial statements into normalized operating metrics and valuation outputs, mirroring the backend modeling work performed in investment banking and equity research.

## Overview
This project is a Python and pandas-based financial analysis tool that automates the ingestion, normalization, and valuation of company financial statements. It integrates income statement, balance sheet, and cash flow data to compute normalized operating metrics and valuation multiples, then exports analyst-ready Excel outputs.

The project is designed to mirror the backend financial modeling work performed by investment banking and equity research analysts prior to building comps or valuation models.

---

## Key Features
- Ingests income statement, balance sheet, and cash flow data from CSV files
- Normalizes earnings by removing one-time items
- Computes core financial metrics including:
  - Normalized EBITDA
  - Free Cash Flow (FCF)
  - ROIC
  - Net Debt
- Calculates valuation metrics including:
  - Enterprise Value
  - EV / Revenue
  - EV / EBITDA
- Exports results to a fully formatted Excel file with:
  - A detailed backend model
  - A clean, presentation-ready summary tab

---

## Project Structure
financial-statement-analysis/
├── data/
│ ├── income_statement.csv
│ ├── balance_sheet.csv
│ └── cash_flow.csv
│
├── data_loader.py
├── normalizer.py
├── metrics.py
├── valuation.py
├── exporter.py
├── run.py
└── README.md

---

## How It Works
1. Raw financial statement data is loaded from CSV files
2. Earnings are normalized to remove non-recurring items
3. Financial statements are merged into a unified model
4. Operating, cash flow, and valuation metrics are calculated
5. Results are exported to Excel for analysis and presentation

All calculations are performed programmatically using pandas, ensuring results update automatically when input data changes.

---

## How to Run
1. Clone the repository
2. Install dependencies:
3. Run the model:

The script will generate a formatted Excel file in the `outputs` directory.

---

## Data
The included CSV files contain simplified example financial statement data for demonstration purposes.  
The model is designed to work with real company financials by replacing the input CSVs with standardized statement data from sources such as Yahoo Finance or SEC filings.

---

## Why This Project
This project demonstrates:
- Financial statement analysis and normalization
- Valuation fundamentals
- Automation of repetitive analyst workflows
- Clean separation of calculation logic and presentation output
- Practical use of pandas for financial modeling

---

