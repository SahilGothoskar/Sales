import pandas as pd
import numpy as np

#import matplotlib.pyplot as plt

#Dataset 1
walmart_path = 'D:\DMDD\Assignment 3\myCity.csv'

walmart_ori = pd.read_csv(walmart_path)
walmart = walmart_ori.copy()

walmart.head()

walmart.info()

#Function to fetch missing values from Dataset 1
def missing_cols(walmart):
    '''prints out columns with its amount of missing values'''
    total = 0
    for col in walmart.columns:
        missing_vals = walmart[col].isnull().sum()
        total += missing_vals
        if missing_vals != 0:
            print(f"{col} => {walmart[col].isnull().sum()}")
    
    if total == 0:
        print("no missing values left")
            
#Missing Columns Values in Walmart Dataframe            
missing_cols(walmart)

def perc_missing(walmart):
    '''prints out columns with missing values with its %'''
    for col in walmart.columns:
        pct = walmart[col].isna().mean() * 100
        if (pct != 0):
            print('{} => {}%'.format(col, round(pct, 2)))

#Percentage Wise Missing Values
perc_missing(walmart)

# Drop unnecessary columns that are not important
colsToDrop = ['StockOfREOs','PrevForeclosed','ForeclosureRatio']

walmart.drop(colsToDrop, axis=1, inplace=True)

#Missing Values Redefined
missing_cols(walmart)

#Percentage Wise Missing Values
perc_missing(walmart)


# imputing with bfill or ffill
walmart['Metro'].bfill(inplace=True)
walmart['Metro'].ffill(inplace=True)
walmart['SizeRank'].bfill(inplace=True)
walmart['SizeRank'].ffill(inplace=True)
walmart['SellForGain'].bfill(inplace=True)
walmart['SellForGain'].ffill(inplace=True)
walmart['ZHVI'].bfill(inplace=True)
walmart['ZHVI'].ffill(inplace=True)
walmart['MoM'].bfill(inplace=True)
walmart['MoM'].ffill(inplace=True)
walmart['ForecastYoYPctChange'].ffill(inplace=True)
walmart['ForecastYoYPctChange'].bfill(inplace=True)
walmart['YoY'].ffill(inplace=True)
walmart['YoY'].ffill(inplace=True)
walmart['Delinquency'].ffill(inplace=True)
walmart['Delinquency'].ffill(inplace=True)
walmart['DaysOnMarket'].ffill(inplace=True)
walmart['DaysOnMarket'].ffill(inplace=True)
walmart['NegativeEquity'].ffill(inplace=True)
walmart['NegativeEquity'].ffill(inplace=True)

#DF Post Cleaning
missing_cols(walmart)


#Cleaned DF 1
print (walmart)

#Cleaned Data Inserted into CSV
csv_data = walmart.to_csv('D:\DMDD\Assignment 3\Cleaned.csv', index = False)


#Dataset 2
walmart_path_1 = 'D:\DMDD\Assignment 3\Walmart.csv'

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






# Import required modules
import csv
import sqlite3

# Connecting to the geeks database
connection = sqlite3.connect('D:\DMDD\Assignment 3\Cleaned_DB.db')

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

# Table Definition
create_table = '''CREATE TABLE IF NOT EXISTS walmart (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
                RegionType VARCHAR NOT NULL, 
                RegionName VARCHAR NOT NULL, 
                City VARCHAR NOT NULL, 
                State VARCHAR NOT NULL, 
                Metro VARCHAR NOT NULL, 
                SizeRank INTEGER NOT NULL, 
                MarketHealthIndex INTEGER NOT NULL, 
                SellForGain INTEGER NOT NULL, 
                ZHVI INTEGER NOT NULL, 
                MoM INTEGER NOT NULL, 
                YoY INTEGER NOT NULL, 
                ForecastYoYPctChange INTEGER NOT NULL, 
                NegativeEquity INTEGER NOT NULL, 
                Delinquency INTEGER NOT NULL,
                DaysOnMarket INTEGER NOT NULL
				);
				'''

# Creating the table into our
# database
cursor.execute(create_table)

# Opening the tweets-records.csv file
file = open('D:\DMDD\Assignment 3\Cleaned.csv' , errors='ignore')

# Reading the contents of the
# tweets-records.csv file
contents = csv.reader(file)



# SQL query to insert data into the
# tweets table
insert_records = "INSERT INTO walmart (RegionType, RegionName,	City,	State,	Metro,	SizeRank,	MarketHealthIndex,	SellForGain,	ZHVI,	MoM,	YoY,	ForecastYoYPctChange, NegativeEquity, Delinquency,	DaysOnMarket) VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

# Importing the contents of the file
# into our tweets table
cursor.executemany(insert_records, contents)

# SQL query to retrieve all data from
# the person table To verify that the
# data of the csv file has been successfully
# inserted into the table
# Change Table to tweets after the SQL
select_all = "SELECT * FROM walmart"
rows = cursor.execute(select_all).fetchall()

# Output to the console screen
for r in rows:
    print(r)

# Committing the changes
connection.commit()

# closing the database connection
connection.close()


            
