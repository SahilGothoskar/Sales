# Walmart Sales Analysis 🛒

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/Tweepy-Twitter%20API-1DA1F2?logo=twitter&logoColor=white" alt="Tweepy" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Cleaning-150458?logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Course-DAMG%206210-orange" alt="Course" />
</p>

---

## 📖 About

A data-management course project analyzing **Walmart store sales** across 45 U.S. locations. The project spans the full data lifecycle — from raw CSV collection and Twitter scraping, through cleaning and normalization, to SQL analysis with views and use-case queries. The goal is to uncover which stores perform best, how holidays and economic factors impact sales, and what public sentiment (via Twitter) reveals about Walmart.

---

## 👥 Team

| Name | NUID | GitHub |
|------|------|--------|
| **Sahil Gothoskar** | 002775631 | [@SahilGothoskar](https://github.com/SahilGothoskar) |
| **Sneha Giranje** | 002785370 | [@snehagiranje27](https://github.com/snehagiranje27) |
| **Arundhati Pathrikar** | 002780632 | [@ArundhatiCat](https://github.com/ArundhatiCat) |

---

## 🗂️ Repository Structure

```
Sales/
├── readme.md                        # ← You are here
├── Assignment_2_30_Questions        # 30 analytical questions about Walmart sales
│
├── Assignment_3/                    # Data cleaning & SQLite ingestion
│   ├── Cleaning_Data.py             # pandas cleaning + SQLite loader for 2 datasets
│   ├── myCity.csv                   # Dataset 1 — housing/market data by city
│   ├── Walmart.csv                  # Dataset 2 — store-level weekly sales
│   ├── Cleaned.csv                  # Cleaned output of Dataset 1
│   ├── Cleaned_DB.db                # SQLite DB with walmart & employment tables
│   ├── SQL and Use cases            # 15 SQL queries + JOIN use cases
│   ├── UML__Assignment_3.png        # UML diagram
│   ├── Readme.md                    # Assignment 3 specific README
│   └── readme.txt                   # Flow-of-program notes
│
├── Twitter_Bot/                     # Twitter scraping pipeline
│   ├── Twitter_Scrape.py            # Tweepy-based tweet scraper → GFG_tweets.csv
│   ├── SQL_Extraction_From_CSV_Load_DB.py  # CSV → SQLite tweets table loader
│   ├── GFG_tweets.csv               # Raw scraped tweets
│   ├── scraped_tweets.csv           # Additional scraped data
│   ├── Tweets_Extracted.db          # SQLite DB with tweets table
│   ├── SQL_Statements.txt           # 12 SQL queries on the tweets table
│   ├── Question_on_SQL_Queries.txt  # Business questions driving the queries
│   ├── Relational_Algebra.txt       # Relational algebra for each query
│   ├── UML.pdf                      # UML diagram
│   └── Assignment3_Text_Formatted_DAMG6210.txt  # Formatted submission text
│
├── Normalization/                   # Database normalization documentation
│   ├── readme.md                    # 1NF → 2NF → 3NF walkthrough per table
│   ├── Views.txt                    # 15 SQL VIEW definitions
│   ├── walmart.jpeg                 # Walmart table screenshot
│   ├── services.jpeg                # Services table screenshot
│   └── employment.jpeg              # Employment table screenshot
│
└── Final/                           # Final consolidated deliverable
    ├── README.md                    # Final project report with UML + screenshots
    ├── SQL_Statements_Twitter_DB.txt # Twitter DB SQL queries
    ├── Views.txt                    # All VIEW definitions
    ├── Tweets_Extracted.db          # Final tweets database
    ├── GFG_tweets*.csv              # Category-split tweet CSVs
    ├── FinalUML.png / FinalUML1.png # Final UML diagrams
    ├── Walmart Sales Database.pdf   # Project report PDF
    ├── sql/*.jpeg                   # SQL output screenshots
    └── *.jpeg / *.png               # Table & view screenshots
```

---

## 📊 Datasets

| # | Dataset | Source | Description |
|---|---------|--------|-------------|
| 1 | `myCity.csv` | Kaggle / Zillow | Housing-market indicators by city — ZHVI, MarketHealthIndex, SellForGain, DaysOnMarket, etc. |
| 2 | `Walmart.csv` | Kaggle | Weekly sales for 45 Walmart stores — includes temperature, fuel price, CPI, unemployment, and holiday flags |
| 3 | `GFG_tweets.csv` | Twitter API (Tweepy) | Scraped tweets about Walmart — username, location, text, hashtags, follower counts |

---

## 🧹 Data Pipeline

```
CSV files (Kaggle)          Twitter API (Tweepy)
       │                            │
       ▼                            ▼
  Cleaning_Data.py           Twitter_Scrape.py
  (pandas: drop cols,        (search by hashtag,
   impute nulls, export)      extract metadata)
       │                            │
       ▼                            ▼
  Cleaned_DB.db              GFG_tweets.csv
  ├─ walmart table                  │
  └─ employment table               ▼
                          SQL_Extraction_From_CSV_Load_DB.py
                                    │
                                    ▼
                            Tweets_Extracted.db
                            └─ tweets table
```

---

## 🔑 Key Analysis Questions

1. Which store has the **highest weekly sales**?
2. Which store's **standard deviation** is the highest — indicating volatile sales?
3. Which store(s) had the **best Q3 growth rate**?
4. Which **holidays** drive sales above non-holiday averages?
5. How does **temperature, fuel price, CPI, and unemployment** correlate with sales?
6. What does **Twitter sentiment** reveal about customer satisfaction?
7. Which cities receive the **most Walmart-related tweets**?
8. How many tweets use **#walfart** (negative sentiment)?

> The full list of 30 business questions is in [`Assignment_2_30_Questions`](./Assignment_2_30_Questions).

---

## 🗄️ Database Schema

### Cleaned_DB.db

| Table | Key Columns | Primary Key |
|-------|-------------|-------------|
| **walmart** | RegionType, RegionName, City, State, Metro, SizeRank, MarketHealthIndex, SellForGain, ZHVI, MoM, YoY, NegativeEquity, Delinquency, DaysOnMarket | `id` (auto) |
| **employment** | Store, Date, Weekly_Sales, Holiday_Flag, Temperature, Fuel_Price, CPI, Unemployment | `id` (auto) |
| **services** | ZHVI, MoM, YoY, NegativeEquity, Delinquency, DaysOnMarket *(split from walmart for normalization)* | `services_id` |

### Tweets_Extracted.db

| Table | Key Columns | Primary Key |
|-------|-------------|-------------|
| **tweets** | username, description, location, following, followers, totaltweets, retweetcount, text, hastags | `id` (auto) |

---

## 🧰 Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3** | All scripts |
| **pandas / NumPy** | Data cleaning, imputation, CSV I/O |
| **Tweepy** | Twitter API v1.1 authentication and search |
| **SQLite 3** | Lightweight relational database |
| **SQL** | 15+ analytical queries, JOINs, aggregate functions, VIEWs |

---

## 🚀 How to Run

### Data Cleaning & SQLite Load

```bash
cd Assignment_3
python Cleaning_Data.py
```

### Twitter Scraping

```bash
cd Twitter_Bot

# 1. Scrape tweets (requires valid Twitter API credentials in the script)
python Twitter_Scrape.py

# 2. Load scraped CSV into SQLite
python SQL_Extraction_From_CSV_Load_DB.py
```

### SQL Queries

Open `Cleaned_DB.db` or `Tweets_Extracted.db` in any SQLite client and run the queries from:
- `Assignment_3/SQL and Use cases` — 15 queries with JOINs
- `Twitter_Bot/SQL_Statements.txt` — 12 Twitter analytics queries
- `Final/Views.txt` — all VIEW definitions

---

## 📐 Normalization

All tables are normalized to **3NF**:
- **1NF** — Atomic values, no repeating groups
- **2NF** — No partial dependencies
- **3NF** — No transitive dependencies

Full walkthrough with screenshots in [`Normalization/readme.md`](./Normalization/readme.md).

---

## 📸 UML Diagrams

| Diagram | Location |
|---------|----------|
| Twitter tables UML | `Final/FinalUML.png` |
| Sales tables UML | `Final/FinalUML1.png` |
| Assignment 3 UML | `Assignment_3/UML__Assignment_3.png` |

---

## ⚠️ Notes

- **Twitter API credentials** in `Twitter_Scrape.py` are placeholder `XXX` values — replace with your own developer keys.
- File paths in `Cleaning_Data.py` use absolute Windows paths (`D:\DMDD\...`). Adjust to your local environment before running.
- The `Cleaned_DB.db` and `Tweets_Extracted.db` files in the repo already contain loaded data for quick exploration.

---

## 📚 Factors in the Sales Dataset

| Column | Description |
|--------|-------------|
| `Store` | Store number (1–45) |
| `Date` | Week of sales |
| `Weekly_Sales` | Total sales for the given store that week |
| `Holiday_Flag` | `1` = holiday week, `0` = non-holiday week |
| `Temperature` | Temperature on the day of sale (°F) |
| `Fuel_Price` | Regional fuel price |
| `CPI` | Consumer Price Index |
| `Unemployment` | Regional unemployment rate |

---

<p align="center">Made with 📊 by Sahil, Sneha & Arundhati — DAMG 6210</p>
