# Assignment 3 — Data Cleaning & SQLite Ingestion 🧹

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/pandas-Data%20Cleaning-150458?logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white" alt="SQLite" />
</p>

---

## 📖 Overview

This assignment covers the full data-ingestion pipeline: **gathering → cleaning → loading → querying**. Two Walmart-related CSV datasets are cleaned using pandas and loaded into a SQLite database for SQL analysis.

---

## 🗂️ Files

| File | Description |
|------|-------------|
| `Cleaning_Data.py` | Python script — cleans both datasets and loads into SQLite |
| `myCity.csv` | Dataset 1 — housing/market data by city (ZHVI, MarketHealthIndex, etc.) |
| `Walmart.csv` | Dataset 2 — weekly store sales with economic indicators |
| `Cleaned.csv` | Cleaned output of Dataset 1 |
| `Cleaned_DB.db` | SQLite database with `walmart` and `employment` tables |
| `SQL and Use cases` | 15 analytical SQL queries with JOINs |
| `UML__Assignment_3.png` | UML diagram for the database schema |

---

## 🔄 Pipeline Flow

```
myCity.csv ──→ Cleaning_Data.py ──→ Cleaned.csv ──→ SQLite: walmart table
                  │                                          │
Walmart.csv ─────┘ (already clean) ──────────────→ SQLite: employment table
                                                          │
                                                   Cleaned_DB.db
```

### Step 1 — Collect Data
Data sourced from Kaggle:
- `myCity.csv` — City-level housing market indicators
- `Walmart.csv` — Store-level weekly sales (45 stores)

### Step 2 — Clean with pandas (`Cleaning_Data.py`)

**Dataset 1 (myCity.csv):**
1. Audit missing values with `missing_cols()` and `perc_missing()` helpers
2. Drop irrelevant columns: `StockOfREOs`, `PrevForeclosed`, `ForeclosureRatio`
3. Impute remaining nulls using backward-fill + forward-fill for: `Metro`, `SizeRank`, `SellForGain`, `ZHVI`, `MoM`, `YoY`, `ForecastYoYPctChange`, `Delinquency`, `DaysOnMarket`, `NegativeEquity`
4. Export cleaned DataFrame to `Cleaned.csv`

**Dataset 2 (Walmart.csv):**
- No missing values — loaded directly

### Step 3 — Load into SQLite
Both datasets are bulk-inserted into `Cleaned_DB.db`:
- `walmart` table — 15 columns (RegionType, RegionName, City, State, Metro, SizeRank, MarketHealthIndex, SellForGain, ZHVI, MoM, YoY, ForecastYoYPctChange, NegativeEquity, Delinquency, DaysOnMarket)
- `employment` table — 8 columns (Store, Date, Weekly_Sales, Holiday_Flag, Temperature, Fuel_Price, CPI, Unemployment)

### Step 4 — SQL Analysis
15 use-case queries in `SQL and Use cases` covering:
- Aggregations (`SUM`, `AVG`, `MIN`, `MAX`)
- Filtered queries (`WHERE`, `BETWEEN`, `HAVING`)
- `INNER JOIN` and `LEFT JOIN` across `walmart` and `services` tables
- Subqueries for max/min lookups

---

## 🚀 How to Run

```bash
cd Assignment_3
python Cleaning_Data.py
```

> **Note:** File paths in the script use absolute Windows paths — adjust to your local environment before running.

---

## 📐 UML Diagram

![UML Diagram](./UML__Assignment_3.png)

---

## 👥 Team

| Name | GitHub |
|------|--------|
| **Sahil Gothoskar** | [@SahilGothoskar](https://github.com/SahilGothoskar) |
| **Sneha Giranje** | [@snehagiranje27](https://github.com/snehagiranje27) |
| **Arundhati Pathrikar** | [@ArundhatiCat](https://github.com/ArundhatiCat) |

# Creating the table into our database
cursor.execute(create_table)

# Opening the Cleaned.csv file
file = open('D:\DMDD\Assignment 3\TEST\Cleaned.csv' , errors='ignore')

# Reading the contents of the Cleaned.csv file
contents = csv.reader(file)


# SQL query to insert data into the walmart table
insert_records = "INSERT INTO walmart (RegionType, RegionName,	City,	State,	Metro,	SizeRank,	MarketHealthIndex,	SellForGain) VALUES( ?, ?, ?, ?, ?, ?, ?, ?)"

# Importing the contents of the file into our walmart table
cursor.executemany(insert_records, contents)

# SQL query to retrieve all data from  the person table To verify that the  data of the csv file has been successfully  inserted into the table
# Change Table to walmart after the SQL
select_all = "SELECT * FROM walmart"
rows = cursor.execute(select_all).fetchall()

# Output to the console screen
for r in rows:
    print(r)

# Committing the changes
connection.commit()

# closing the database connection
connection.close()



#Dataset 2
walmart_path_1 = 'D:\DMDD\Assignment 3\TEST\mycity_8_16.csv'

walmart_ori_1 = pd.read_csv(walmart_path_1)
walmart_1 = walmart_ori_1.copy()

walmart_1.head()

walmart_1.info()

#Function to fetch missing values from Dataset 1
def missing_cols(walmart_1):
    '''prints out columns with its amount of missing values'''
    total = 0
    for col in walmart_1.columns:
        missing_vals = walmart_1[col].isnull().sum()
        total += missing_vals
        if missing_vals != 0:
            print(f"{col} => {walmart_1[col].isnull().sum()}")
    
    if total == 0:
        print("no missing values left")

missing_cols(walmart_1)


def perc_missing(walmart_1):
    '''prints out columns with missing values with its %'''
    for col in walmart_1.columns:
        pct = walmart_1[col].isna().mean() * 100
        if (pct != 0):
            print('{} => {}%'.format(col, round(pct, 2)))

perc_missing(walmart_1)

# Drop unnecessary columns that are not important
colsToDrop = ['StockOfREOs','PrevForeclosed','ForeclosureRatio']

walmart_1.drop(colsToDrop, axis=1, inplace=True)

#Missing Values Redefined
missing_cols(walmart_1)

#Percentage Wise Missing Values
perc_missing(walmart_1)

# imputing with bfill or ffill
walmart_1['ZHVI'].bfill(inplace=True)
walmart_1['ZHVI'].ffill(inplace=True)
walmart_1['MoM'].bfill(inplace=True)
walmart_1['MoM'].ffill(inplace=True)
walmart_1['ForecastYoYPctChange'].ffill(inplace=True)
walmart_1['ForecastYoYPctChange'].bfill(inplace=True)
walmart_1['YoY'].ffill(inplace=True)
walmart_1['YoY'].ffill(inplace=True)
walmart_1['Delinquency'].ffill(inplace=True)
walmart_1['Delinquency'].ffill(inplace=True)
walmart_1['DaysOnMarket'].ffill(inplace=True)
walmart_1['DaysOnMarket'].ffill(inplace=True)
walmart_1['NegativeEquity'].ffill(inplace=True)
walmart_1['NegativeEquity'].ffill(inplace=True)

#DF Post Cleaning
missing_cols(walmart_1)


#Cleaned DF 1
print (walmart_1)

#Converting DataFrame to CSV
csv_data = walmart_1.to_csv('D:\DMDD\Assignment 3\TEST\Cleaned_1.csv', index = False)

# Connecting to the Cleaned database
connection = sqlite3.connect('D:\DMDD\Assignment 3\TEST\Cleaned_TEST_DB.db')

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

# Table Definition
create_table = '''CREATE TABLE IF NOT EXISTS services (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
                ZHVI INTEGER NOT NULL, 
                MoM INTEGER NOT NULL, 
                YoY INTEGER NOT NULL, 
                ForecastYoYPctChange INTEGER NOT NULL, 
                NegativeEquity INTEGER NOT NULL, 
                Delinquency INTEGER NOT NULL,
                DaysOnMarket INTEGER NOT NULL
				);
				'''

# Creating the table into our  database
cursor.execute(create_table)

# Opening the Cleaned_1.csv file
file = open('D:\DMDD\Assignment 3\TEST\Cleaned_1.csv' , errors='ignore')

# Reading the contents of the Cleaned_1.csv file
contents = csv.reader(file)


# SQL query to insert data into the services table
insert_records = "INSERT INTO services (ZHVI, MoM, YoY, ForecastYoYPctChange, NegativeEquity, Delinquency, DaysOnMarket) VALUES( ?, ?, ?, ?, ?, ?, ?)"

# Importing the contents of the file  into our tweets table
cursor.executemany(insert_records, contents)

# SQL query to retrieve all data from  the person table To verify that the data of the csv file has been successfully inserted into the table
# Change Table to services after the SQL
select_all = "SELECT * FROM services"
rows = cursor.execute(select_all).fetchall()

# Output to the console screen
for r in rows:
    print(r)

# Committing the changes
connection.commit()

# closing the database connection
connection.close()


#Dataset 3
walmart_path_2 = 'D:\DMDD\Assignment 3\Walmart.csv'

walmart_ori_2 = pd.read_csv(walmart_path_2)
walmart_2 = walmart_ori_2.copy()

walmart_2.head()

walmart_2.info()

#Function to fetch missing values from Dataset 1
def missing_cols(walmart_2):
    '''prints out columns with its amount of missing values'''
    total = 0
    for col in walmart_2.columns:
        missing_vals = walmart_2[col].isnull().sum()
        total += missing_vals
        if missing_vals != 0:
            print(f"{col} => {walmart_1[col].isnull().sum()}")
    
    if total == 0:
        print("no missing values left")

missing_cols(walmart_2)

# Connecting to the Cleaned database
connection = sqlite3.connect('D:\DMDD\Assignment 3\Cleaned_DB.db')

# Creating a cursor object to execute SQL queries on a database table
cursor = connection.cursor()

# Table Definition
create_table = '''CREATE TABLE IF NOT EXISTS employment (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
                Store INTEGER NOT NULL,
                Date INTEGER NOT NULL,
                Weekly_Sales INTEGER NOT NULL,	
                Holiday_Flag INTEGER NOT NULL,
                Temperature	INTEGER NOT NULL,
                Fuel_Price INTEGER NOT NULL,
                CPI INTEGER NOT NULL,
                Unemployment INTEGER NOT NULL
				);
				'''

# Creating the table into our database
cursor.execute(create_table)

# Opening the Walmart.csv file
file = open('D:\DMDD\Assignment 3\Walmart.csv' , errors='ignore')

# Reading the contents of the Walmart.csv file
contents = csv.reader(file)

# SQL query to insert data into the employment table
insert_records = "INSERT INTO employment (Store, Date, Weekly_Sales, Holiday_Flag, Temperature, Fuel_Price, CPI, Unemployment) VALUES( ?, ?, ?, ?, ?, ?, ?, ?)"

# Importing the contents of the file into our employment table
cursor.executemany(insert_records, contents)

# SQL query to retrieve all data from the person table To verify that the data of the csv file has been successfully inserted into the table
# Change Table to tweets after the SQL
select_all = "SELECT * FROM employment"
rows = cursor.execute(select_all).fetchall()

# Output to the console screen
for r in rows:
    print(r)

# Committing the changes
connection.commit()

# closing the database connection
connection.close()



```

## Use Cases and SQL Queries

```sh 

1.Find total weekly sales of each store.
SQL--> SELECT Store , SUM(Weekly_Sales) as Total_weeklysales FROM employment GROUP BY Store;

2.Find dates on which Walmart store had Fuel_Price > 3.5 and Holiday_Flag was 0
SQL-->  SELECT Store, Date , Fuel_Price, Holiday_Flag FROM employment WHERE Holiday_Flag=0 AND Fuel_Price > 3.5;

3.Select min of Unemployment of store 1 and sales between 1542561.09 and 1606629.58 
SQL-->  SELECT MIN(Unemployment), Store from employment WHERE STORE=1 AND Weekly_Sales BETWEEN 1542561.09 AND 1606629.58 GROUP BY Store;

4.Find average weekly sales of each store.
SQL-->  SELECT AVG(Weekly_Sales), Store from employment GROUP BY Store;

5.list the number of customers in each country. Only include STORES with less than 3 Holiday_flag
SQL-->   SELECT Store, SUM(Holiday_Flag) FROM employment GROUP BY Store HAVING SUM(Holiday_Flag) >9;

6.Show all the DaysOnMarket where CITY is Phoenix
SQL-->  SELECT walmart.RegionName, walmart.City, services.DaysOnMarket  from  walmart INNER JOIN services ON walmart.Walmart_id = services.services_id  where City="Phoenix";

7.Finding out Maximum SizeRank, RegionName, City where DaysOnMarket=106
SQL-->  SELECT walmart.SizeRank, walmart.RegionName, walmart.City, services.DaysOnMarket from walmart INNER JOIN services ON walmart.Walmart_id = services.services_id  WHERE SizeRank=(SELECT MAX(SizeRank) from walmart) AND  services.DaysOnMarket=106;

8.Finding cities and region where  NegativeEquity < Delinquency
SQL-->  SELECT walmart.RegionName, walmart.City, services.NegativeEquity, services.Delinquency from walmart INNER JOIN services ON walmart.Walmart_id = services.services_id WHERE  NegativeEquity < Delinquency;

9.Show all cities an regions with any DaysOnMarket they might have
SQL-->  SELECT walmart.RegionName, walmart.City,  services.DaysOnMarket FROM walmart LEFT JOIN services ON walmart.Walmart_id = services.services_id;

10.Show all cities, regions, state with All DaysOnMarket in the table
SQL-->  SELECT walmart.RegionName, walmart.City, walmart.State, services.DaysOnMarket FROM walmart LEFT JOIN services ON walmart.Walmart_id = services.services_id UNION SELECT walmart.RegionName, walmart.City, walmart.State, services.DaysOnMarket FROM walmart LEFT JOIN services ON walmart.Walmart_id = services.services_id ;

11.Show the list of NegativeEquity, Delinquency, regions in Massachusetts state and city is Boston 
SQL-->  SELECT walmart.RegionName, walmart.City, services.NegativeEquity, services.Delinquency  from  walmart INNER JOIN services ON walmart.Walmart_id = services.services_id WHERE City=“Boston";

12.Finding out Maximum SellForGain, RegionName, City where ZHVI >= 695600
SQL-->  SELECT walmart.SellForGain, walmart.RegionName, walmart.City, services.ZHVI from walmart INNER JOIN services ON walmart.Walmart_id = services.services_id WHERE SellForGain=(SELECT MAX(SellForGain) from walmart) AND services.ZHVI =190900;


13.Show DaysOnMarket in each state
SQL-->  SELECT walmart.State, SUM(services.DaysOnMarket) from walmart INNER JOIN services ON walmart.Walmart_id = services.services_id GROUP BY State;

14.Select store which has the highest weekly sale on this 05-02-2010 date
SQL-->  SELECT Store, Weekly_Sales, Date from employment where Date = 05-02-2010  AND Weekly_Sales=(SELECT MAX(Weekly_Sales) from employment );

15.Finding out Minimum MarketHealthIndex, RegionName, City where MoM=1.00791936645068
SQL--> SELECT walmart.MarketHealthIndex, walmart.RegionName, walmart.City, services.MoM from walmart INNER JOIN services ON walmart.Walmart_id = services.services_id WHERE MarketHealthIndex=(SELECT MAX(MarketHealthIndex) from walmart) OR MoM= 1.00791936645068;


```

Sneha Giranje (002785370)
Arundhati Pathrikar (002780632)
Sahil Gothoskar (002775631)







