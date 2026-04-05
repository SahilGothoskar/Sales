# Final Deliverable — Walmart Sales Database 📦

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/Tweepy-Twitter%20API-1DA1F2?logo=twitter&logoColor=white" alt="Tweepy" />
  <img src="https://img.shields.io/badge/pandas-Data%20Cleaning-150458?logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Course-DAMG%206210-orange" alt="Course" />
</p>

---

## 👥 Team

| Name | NUID | GitHub |
|------|------|--------|
| **Sahil Gothoskar** | 002775631 | [@SahilGothoskar](https://github.com/SahilGothoskar) |
| **Sneha Giranje** | 002785370 | [@snehagiranje27](https://github.com/snehagiranje27) |
| **Arundhati Pathrikar** | 002780632 | [@ArundhatiCat](https://github.com/ArundhatiCat) |

---

## 📖 Project Description

Walmart is one of the leading retailers in the United States with ~4,742 stores. This project analyzes historical sales data for 45 Walmart stores across different regions to determine which locations perform best, how holidays and economic factors impact weekly sales, and what Twitter sentiment reveals about customer satisfaction.

Walmart holds promotional markdown events before the **Super Bowl, Labor Day, Thanksgiving, and Christmas** — holiday weeks are weighted 5× more heavily in the evaluation.

---

## 🎯 Goals

- Identify the **highest-revenue** store and the store with the **most volatile** sales (highest standard deviation)
- Determine which stores had the **best Q3 growth rate**
- Analyze which **holidays** drive above-average sales
- Provide **monthly and semester** sales snapshots
- Combine Kaggle sales data with **Twitter sentiment** for a comprehensive view

---

## 📐 UML Diagrams

### Twitter Tables

![Twitter UML](./FinalUML.png)

### Sales / Market Tables

![Sales UML](./FinalUML1.png)

---

## 🗄️ Database Tables

### Twitter-Sourced Tables

| Table | Description | Screenshot |
|-------|-------------|------------|
| **Giftcards** | Tweets with hashtags about Walmart gift card promotions | ![](./tweets_giftcards.png) |
| **Tweets** | General Walmart-related tweets | ![](./tweets_table.png) |
| **Delivery** | Tweets about Walmart delivery service | ![](./tweets_delivery.png) |
| **Fart** | Negative-sentiment tweets (#walfart) from dissatisfied customers | ![](./tweets_fart.png) |

### Cleaned & Normalized Sales Tables

| Table | Primary Key | Foreign Key | Description |
|-------|-------------|-------------|-------------|
| **Employment** | `Employment_Id` | `Services_Id` | Store-level weekly sales, holiday flag, temperature, fuel price, CPI, unemployment |
| **Services** | `Services_Id` | `Employment_Id` | Market indicators — ZHVI, MoM, YoY, NegativeEquity, Delinquency, DaysOnMarket |
| **Walmart** | `Walmart_Id` | — | Store regions — RegionType, City, State, Metro, SizeRank, MarketHealthIndex, SellForGain |

| Table | Screenshot |
|-------|------------|
| **Employment** | ![](./employment.jpeg) |
| **Services** | ![](./services.jpeg) |
| **Walmart** | ![](./walmart.jpeg) |

> All tables are normalized to **3NF** — see the [Normalization README](../Normalization/readme.md) for the full walkthrough.

---

## 🔍 SQL Queries (1–15: Sales DB)

| # | Query | SQL |
|---|-------|-----|
| 1 | Total weekly sales per store | `SELECT Store, SUM(Weekly_Sales) AS Total_weeklysales FROM employment GROUP BY Store` |
| 2 | Stores with Fuel_Price > 3.5 on non-holidays | `SELECT Store, Date, Fuel_Price, Holiday_Flag FROM employment WHERE Holiday_Flag=0 AND Fuel_Price > 3.5` |
| 3 | Min unemployment for Store 1 in a sales range | `SELECT MIN(Unemployment), Store FROM employment WHERE STORE=1 AND Weekly_Sales BETWEEN 1542561.09 AND 1606629.58 GROUP BY Store` |
| 4 | Average weekly sales per store | `SELECT AVG(Weekly_Sales), Store FROM employment GROUP BY Store` |
| 5 | Stores with holiday flag sum > 9 | `SELECT Store, SUM(Holiday_Flag) FROM employment GROUP BY Store HAVING SUM(Holiday_Flag) > 9` |
| 6 | DaysOnMarket in Phoenix (JOIN) | `... INNER JOIN services ON walmart.Walmart_id = services.services_id WHERE City="Phoenix"` |
| 7 | Max SizeRank where DaysOnMarket = 106 | `... WHERE SizeRank=(SELECT MAX(SizeRank) ...) AND services.DaysOnMarket=106` |
| 8 | Cities where NegativeEquity < Delinquency | `... WHERE NegativeEquity < Delinquency` |
| 9 | All cities with DaysOnMarket (LEFT JOIN) | `SELECT walmart.RegionName, walmart.City, services.DaysOnMarket FROM walmart LEFT JOIN services ...` |
| 10 | All cities/regions/states with DaysOnMarket (UNION) | `... LEFT JOIN ... UNION SELECT ...` |
| 11 | NegativeEquity & Delinquency in Boston | `... WHERE City="Boston"` |
| 12 | Max SellForGain by ZHVI threshold | `... WHERE SellForGain=(SELECT MAX(SellForGain) ...) AND services.ZHVI=190900` |
| 13 | DaysOnMarket totals by state | `... GROUP BY State` |
| 14 | Highest weekly sale on 05-02-2010 | `... WHERE Date = 05-02-2010 AND Weekly_Sales=(SELECT MAX(Weekly_Sales) ...)` |
| 15 | Min MarketHealthIndex by MoM threshold | `... WHERE MarketHealthIndex=(SELECT MAX(...)) OR MoM=1.00791936645068` |

### SQL Output Screenshots

| | | |
|---|---|---|
| ![](./sql1.png) | ![](./sql2.png) | ![](./sql3.png) |
| ![](./sql4.png) | ![](./sql5.png) | ![](./sql6.png) |
| ![](./sql7.png) | ![](./sql8.png) | ![](./sql9.png) |
| ![](./sql10.jpeg) | ![](./sql11.jpeg) | ![](./sql12.jpeg) |
| ![](./sql13.jpeg) | ![](./sql14.jpeg) | ![](./sql15.jpeg) |
| ![](./sql/1.jpeg) | ![](./sql/2.jpeg) | ![](./sql/3.jpeg) |
| ![](./sql/4.jpeg) | ![](./sql/5.jpeg) | ![](./sql/6.jpeg) |
| ![](./sql/7.jpeg) | ![](./sql/8.jpeg) | ![](./sql/9.jpeg) |

---

## 🐦 SQL Queries (16–30: Twitter DB)

| # | Query | Description |
|---|-------|-------------|
| 16 | `CREATE TABLE tweets (...)` | Create the tweets table schema |
| 17 | `SELECT (*) FROM tweets WHERE description = "walmart delivery"` | Tweets about Walmart delivery |
| 18 | `SELECT COUNT(*) ... WHERE hastags = "#walmartsales"` | Tweet count for #walmartsales |
| 19 | `SELECT COUNT(DISTINCT hastags) ...` | Unique hashtags related to Walmart/sales |
| 20 | `SELECT COUNT(*) ... WHERE description = "walmart happy customers"` | Positive sentiment tweets |
| 21 | `SELECT COUNT(*) ... WHERE description = "walmartdelivery"` | Delivery tweet count |
| 22 | `SELECT * ... WHERE description = "EmmaWatson" ... hashtags = "#walmartgiftcards"` | Influencers promoting gift cards |
| 23 | `SELECT location, COUNT(totaltweets) ... GROUP BY location` | Location with most tweets |
| 24 | `SELECT location, COUNT(totaltweets) ... WHERE description LIKE '%HP Pavilion%'` | HP Pavilion tweet locations |
| 25 | `SELECT COUNT(*) ... WHERE hastags LIKE '%walfart%'` | Negative sentiment (#walfart) count |
| 26 | `SELECT * ... WHERE description = "walmart distribution centre"` | Distribution center tweets |
| 27 | `SELECT COUNT(*) ... WHERE description = "no walmart yes target"` | Customers switching to Target |
| 28 | `SELECT COUNT(*) ... WHERE description LIKE '%latedelivery%' OR '%lost%'` | Frustrated customers (late/lost orders) |
| 29 | `SELECT location, COUNT(*) ... WHERE '%win%' OR '%offer%' ... LIMIT 3` | Top 3 cities for gift card tweets |
| 30 | `SELECT username, COUNT(totaltweets) ... ORDER BY totaltweets LIMIT 3` | Top 3 most active Walmart tweeters |

---

## 👁️ SQL VIEWs

15 VIEWs were created for reusable analytics:

| # | View Name | Purpose |
|---|-----------|---------|
| 1 | `total_sales` | Total weekly sales per store |
| 2 | `fuelprice` | Non-holiday dates with high fuel prices |
| 3 | `Min_unemployemnt` | Min unemployment for a filtered store |
| 4 | `Avg_weekly_sales` | Average weekly sales per store |
| 5 | `Sum_holiday_flag` | Stores by holiday flag sum |
| 6 | `DOM_Phoenix` | DaysOnMarket for Phoenix |
| 7 | `DOM` | Max SizeRank by DaysOnMarket |
| 8 | `sales_services` | NegativeEquity vs Delinquency |
| 9 | `All_dom` | All regions with DaysOnMarket |
| 10 | `Services_dom` | All regions/states with DaysOnMarket |
| 11 | `negative_equity` | Boston NegativeEquity & Delinquency |
| 12 | `ZHVI` | Max SellForGain by ZHVI |
| 13 | `DOM_states` | DaysOnMarket totals by state |
| 14 | `weekly_sales` | Highest sale on a specific date |
| 15 | `min_MHI` | Min MarketHealthIndex by MoM |

### View Output Screenshots

| | |
|---|---|
| ![](./views_created.png) | |
| ![](./sql/View-SS1.png) | ![](./sql/View-SS2.png) |
| ![](./sql/View-SS3.png) | ![](./sql/View-SS4.png) |
| ![](./sql/View-SS5.png) | ![](./sql/View-SS6.png) |
| ![](./sql/View-SS7.png) | ![](./sql/View-SS8.png) |
| ![](./sql/View-SS9.png) | ![](./sql/View-SS10.png) |
| ![](./sql/View-SS11.png) | ![](./sql/View-SS12.png) |
| ![](./sql/View-SS13.png) | ![](./sql/View-SS14.png) |
| ![](./sql/View-SS15.png) | |

---

## 🛠️ Steps Performed

1. Investigated datasets from Kaggle and other legitimate data sources
2. Verified dataset authenticity and completeness
3. Created Python scripts to clean CSV data and load it into SQLite tables
4. Assigned primary/foreign key constraints across tables
5. Executed SQL statements to answer the 30 use-case questions
6. Cleaned database inconsistencies using pandas (drop columns, impute nulls)
7. Created ER and UML diagrams for the database schema
8. Defined SQL VIEWs for reusable data retrieval
9. Normalized all tables to 3NF

---

## 📝 Business Use Cases (30 Questions)

<details>
<summary>Click to expand full list</summary>

1. Which retailer has the highest sales?
2. Which retailer's standard deviation is the highest?
3. Determine the ratio of the mean to the standard deviation.
4. Which retailer(s) has/have the best quarterly growth rate in Q3?
5. Which holidays have more sales than the average non-holiday season?
6. Monthly and semester sales snapshots.
7. Which retailers are closest to public transportation?
8. What other stores are located near Walmart retailers?
9. Summary of elements that boost or depress sales.
10. Category with most customer traffic at Walmart.
11. Which retailer buys from the farmers market?
12. Most cost-effective logistics for restocking.
13. Employee attrition rate.
14. ETA for retailers to restock supplies.
15. Typical billing line wait time.
16. Walmart's employee education hiring standard.
17. Typical employee happiness index.
18. Does the retailer act on customer feedback?
19. Least delivery time by shipping vendors.
20. Do retailers ship outside their jurisdiction?
21. Membership requirements — is SSN required?
22. Are groceries available for dietary restrictions (Kosher, Vegan, etc.)?
23. Is the store accessible for disabled, elderly, and pregnant visitors?
24. Do retailers develop marketing strategies?
25. Percentage of goods that expire unsold.
26. What products does Walmart lack and why?
27. How many competitors are nearby? Impact on sales?
28. Online vs in-store shopping preference.
29. How frequently does the retailer advertise?
30. Impact of advertisement on sales.
31. Is the retailer in a prime city location?
32. Is parking available?
33. Is self-checkout available?

</details>

---

<p align="center">Made with 📊 by Sahil, Sneha & Arundhati — DAMG 6210</p>
