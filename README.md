# Micro Center Webscraper using BeautifulSoup to Database
## Overview
A simple microcenter scraper to extract product details and prices from Microcenter.com using Python Requests and BeautifulSoup.
This project is to build a simple ETL pipeline to fetch real-time data via webscrape and store that data into a database. For this case we have scraped the Micro Center product line and the database we used is MySQL database.

## Config File
```
[mysqldb]
host = <HOST NAME>
db = <DATABASE NAME>
user = <USERNAME>
pass = <PASSWORD>
```

## Files
```
data-analysis.ipynb - Simple data analysis of collected data extracted from MySQL database

output.csv - Temporary store of collected data before preprocessing

pipeline.py - Contains class to handle ETL process (i.e. dropping, creating, loading, and inserting tables)

scraper.py - Contains class to parse and handle results returned from the url request

sql_queries.py - Contains queries to create schema and tables in MySQL database and insert statement format

url.py - Contains url information for the webscraper to search and collect data
```

## How to Run
```
python scraper.py
python pipeline.py
```

## Results
![RESULTS](https://github.com/justingee193/microcenter-scraper/blob/master/Results.PNG)