Assignment 3 — Data Cleaning & SQLite Ingestion
=================================================

Tools: Python 3, pandas, SQLite3

Datasets:
  1. myCity.csv  — https://www.kaggle.com/datasets/yasserh/walmart-dataset?resource=download
  2. Walmart.csv — https://www.kaggle.com/code/avelinocaio/walmart-store-sales-forecasting

Pipeline:
  myCity.csv  → clean (drop cols, impute nulls) → Cleaned.csv → walmart & services tables
  Walmart.csv → load directly                                 → employment table
  All tables stored in Cleaned_DB.db

See Readme.md for full details, SQL queries, and UML diagram.

Team:
  - Sahil Gothoskar   (@SahilGothoskar)
  - Sneha Giranje     (@snehagiranje27)
  - Arundhati Pathrikar (@ArundhatiCat)
