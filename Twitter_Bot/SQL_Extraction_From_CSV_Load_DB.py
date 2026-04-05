"""
SQL_Extraction_From_CSV_Load_DB.py — CSV → SQLite Ingestion
=============================================================
Reads the scraped tweets CSV (GFG_tweets.csv) produced by Twitter_Scrape.py,
creates a `tweets` table in Tweets_Extracted.db, and bulk-inserts all rows.

Schema:
  tweets(id, username, description, location, following, followers,
         totaltweets, retweetcount, text, hastags)

Authors: Sneha Giranje, Arundhati Pathrikar, Sahil Gothoskar
Course : DAMG 6210
"""

import csv
import sqlite3

# ---------------------------------------------------------------------------
# Connect to (or create) the SQLite database
# ---------------------------------------------------------------------------
connection = sqlite3.connect('Tweets_Extracted.db')
cursor = connection.cursor()

# ---------------------------------------------------------------------------
# Create the tweets table
# ---------------------------------------------------------------------------
create_table = '''CREATE TABLE tweets(
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    username     VARCHAR NOT NULL,
    description  VARCHAR NOT NULL,
    location     VARCHAR NOT NULL,
    following    INTEGER NOT NULL,
    followers    INTEGER NOT NULL,
    totaltweets  INTEGER NOT NULL,
    retweetcount INTEGER NOT NULL,
    text         VARCHAR NOT NULL,
    hastags      VARCHAR NOT NULL
);'''

cursor.execute(create_table)

# ---------------------------------------------------------------------------
# Read the scraped CSV and bulk-insert into the tweets table
# ---------------------------------------------------------------------------
file = open('GFG_tweets.csv', errors='ignore')
contents = csv.reader(file)

insert_records = """INSERT INTO tweets
    (username, description, location, following, followers,
     totaltweets, retweetcount, text, hastags)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""

cursor.executemany(insert_records, contents)

# ---------------------------------------------------------------------------
# Verify the insert by printing all rows
# ---------------------------------------------------------------------------
rows = cursor.execute("SELECT * FROM tweets").fetchall()
for r in rows:
    print(r)

# ---------------------------------------------------------------------------
# Commit and close
# ---------------------------------------------------------------------------
connection.commit()
connection.close()