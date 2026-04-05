"""
Cleaning_Data.py — Walmart Sales Data Cleaning & SQLite Loader
================================================================
This script handles two separate Walmart datasets:

  Dataset 1 (myCity.csv):
    - Housing-market data by region/city (ZHVI, MarketHealthIndex, etc.)
    - Drop irrelevant columns, impute missing values with forward/backward fill.
    - Export cleaned data to CSV and load into SQLite `walmart` table.

  Dataset 2 (Walmart.csv):
    - Store-level weekly sales with economic indicators.
    - Already clean — loaded directly into SQLite `employment` table.

Both tables land in Cleaned_DB.db for downstream SQL analysis and Views.

Authors: Sneha Giranje, Arundhati Pathrikar, Sahil Gothoskar
Course : DAMG 6210
"""

import pandas as pd
import numpy as np

# ──────────────────────────────────────────────────────────────────────────────
# DATASET 1 — Housing / City-Level Market Data (myCity.csv)
# ──────────────────────────────────────────────────────────────────────────────

walmart_path = 'D:\DMDD\Assignment 3\myCity.csv'

# Load the raw CSV into a DataFrame and work on a copy to preserve the original
walmart_ori = pd.read_csv(walmart_path)
walmart = walmart_ori.copy()

# Quick peek at the first rows and column dtypes
walmart.head()
walmart.info()


# ---------- Utility: identify missing values ----------

def missing_cols(walmart):
    """Print every column that has at least one null value and its count."""
    total = 0
    for col in walmart.columns:
        missing_vals = walmart[col].isnull().sum()
        total += missing_vals
        if missing_vals != 0:
            print(f"{col} => {walmart[col].isnull().sum()}")
    if total == 0:
        print("no missing values left")


def perc_missing(walmart):
    """Print the percentage of missing values per column (non-zero only)."""
    for col in walmart.columns:
        pct = walmart[col].isna().mean() * 100
        if pct != 0:
            print('{} => {}%'.format(col, round(pct, 2)))


# ---------- Step 1: Audit missing values ----------
missing_cols(walmart)
perc_missing(walmart)

# ---------- Step 2: Drop columns irrelevant to the analysis ----------
colsToDrop = ['StockOfREOs', 'PrevForeclosed', 'ForeclosureRatio']
walmart.drop(colsToDrop, axis=1, inplace=True)

# Re-check after dropping
missing_cols(walmart)
perc_missing(walmart)

# ---------- Step 3: Impute remaining nulls (backward + forward fill) ----------
# Using bfill then ffill ensures no edge-row NaNs remain.
fill_cols = [
    'Metro', 'SizeRank', 'SellForGain', 'ZHVI', 'MoM',
    'ForecastYoYPctChange', 'YoY', 'Delinquency',
    'DaysOnMarket', 'NegativeEquity',
]
for col in fill_cols:
    walmart[col].bfill(inplace=True)
    walmart[col].ffill(inplace=True)

# ---------- Step 4: Verify no missing values remain ----------
missing_cols(walmart)

# Preview the cleaned DataFrame
print(walmart)

# ---------- Step 5: Export cleaned data to CSV ----------
csv_data = walmart.to_csv('D:\DMDD\Assignment 3\Cleaned_1.csv', index=False)


# ──────────────────────────────────────────────────────────────────────────────
# Load Dataset 1 into SQLite — table: walmart
# ──────────────────────────────────────────────────────────────────────────────

import csv
import sqlite3

connection = sqlite3.connect('D:\DMDD\Assignment 3\Cleaned_DB.db')
cursor = connection.cursor()

# Create the walmart table (housing / market data by region)
create_table = '''CREATE TABLE IF NOT EXISTS walmart (
    id                    INTEGER PRIMARY KEY AUTOINCREMENT,
    RegionType            VARCHAR NOT NULL,
    RegionName            VARCHAR NOT NULL,
    City                  VARCHAR NOT NULL,
    State                 VARCHAR NOT NULL,
    Metro                 VARCHAR NOT NULL,
    SizeRank              INTEGER NOT NULL,
    MarketHealthIndex     INTEGER NOT NULL,
    SellForGain           INTEGER NOT NULL,
    ZHVI                  INTEGER NOT NULL,
    MoM                   INTEGER NOT NULL,
    YoY                   INTEGER NOT NULL,
    ForecastYoYPctChange  INTEGER NOT NULL,
    NegativeEquity        INTEGER NOT NULL,
    Delinquency           INTEGER NOT NULL,
    DaysOnMarket          INTEGER NOT NULL
);'''

cursor.execute(create_table)

# Read cleaned CSV and bulk-insert into the table
file = open('D:\DMDD\Assignment 3\Cleaned.csv', errors='ignore')
contents = csv.reader(file)

insert_records = """INSERT INTO walmart
    (RegionType, RegionName, City, State, Metro, SizeRank,
     MarketHealthIndex, SellForGain, ZHVI, MoM, YoY,
     ForecastYoYPctChange, NegativeEquity, Delinquency, DaysOnMarket)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

cursor.executemany(insert_records, contents)

# Verify the insert by selecting all rows
rows = cursor.execute("SELECT * FROM walmart").fetchall()
for r in rows:
    print(r)

connection.commit()
connection.close()


# ──────────────────────────────────────────────────────────────────────────────
# DATASET 2 — Store-Level Weekly Sales (Walmart.csv)
# ──────────────────────────────────────────────────────────────────────────────

walmart_path_1 = 'D:\DMDD\Assignment 3\Walmart.csv'

walmart_ori_1 = pd.read_csv(walmart_path_1)
walmart_1 = walmart_ori_1.copy()

walmart_1.head()
walmart_1.info()


def missing_cols(walmart_1):
    """Print columns with missing values for Dataset 2."""
    total = 0
    for col in walmart_1.columns:
        missing_vals = walmart_1[col].isnull().sum()
        total += missing_vals
        if missing_vals != 0:
            print(f"{col} => {walmart_1[col].isnull().sum()}")
    if total == 0:
        print("no missing values left")


# Audit — Dataset 2 is already clean
missing_cols(walmart_1)


# ──────────────────────────────────────────────────────────────────────────────
# Load Dataset 2 into SQLite — table: employment
# ──────────────────────────────────────────────────────────────────────────────

connection = sqlite3.connect('D:\DMDD\Assignment 3\Cleaned_DB.db')
cursor = connection.cursor()

# Create the employment table (store-level weekly sales + economic indicators)
create_table = '''CREATE TABLE IF NOT EXISTS employment (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    Store         INTEGER NOT NULL,
    Date          INTEGER NOT NULL,
    Weekly_Sales  INTEGER NOT NULL,
    Holiday_Flag  INTEGER NOT NULL,
    Temperature   INTEGER NOT NULL,
    Fuel_Price    INTEGER NOT NULL,
    CPI           INTEGER NOT NULL,
    Unemployment  INTEGER NOT NULL
);'''

cursor.execute(create_table)

# Read the raw Walmart.csv and bulk-insert
file = open('D:\DMDD\Assignment 3\Walmart.csv', errors='ignore')
contents = csv.reader(file)

insert_records = """INSERT INTO employment
    (Store, Date, Weekly_Sales, Holiday_Flag, Temperature,
     Fuel_Price, CPI, Unemployment)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""

cursor.executemany(insert_records, contents)

# Verify the insert
rows = cursor.execute("SELECT * FROM employment").fetchall()
for r in rows:
    print(r)

connection.commit()
connection.close()







