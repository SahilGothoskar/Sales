# Import required modules
import csv
import sqlite3

# Connecting to the geeks database
connection = sqlite3.connect('Tweets_Extracted.db')

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

# Table Definition
create_table = '''CREATE TABLE tweets(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				username VARCHAR NOT NULL,
				description VARCHAR NOT NULL,
				location VARCHAR NOT NULL,
				following INTEGER NOT NULL,
				followers INTEGER NOT NULL,
				totaltweets INTEGER NOT NULL,
				retweetcount INTEGER NOT NULL,
				text VARCHAR NOT NULL,
				hastags VARCHAR NOT NULL
				);
				'''

# Creating the table into our
# database
cursor.execute(create_table)

# Opening the tweets-records.csv file
file = open('GFG_tweets.csv' , errors='ignore')

# Reading the contents of the
# tweets-records.csv file
contents = csv.reader(file)


# SQL query to insert data into the
# tweets table
insert_records = "INSERT INTO tweets (id,username,description,location,following,followers,totaltweets,retweetcount,text,hastags) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ? )"

# Importing the contents of the file
# into our tweets table
cursor.executemany(insert_records, contents)

# SQL query to retrieve all data from
# the tweets table To verify that the
# data of the csv file has been successfully
# inserted into the table
select_all = "SELECT * FROM tweets"
rows = cursor.execute(select_all).fetchall()

# Output to the console screen
for r in rows:
	print(r)

# Committing the changes
connection.commit()

# closing the database connection
connection.close()
