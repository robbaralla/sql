# Create SQLite3 database and table

#import SQLite3 library
import sqlite3

#create new db if it doesn't exist yet
conn=sqlite3.connect("new.db")

#get a cursor object used to execute SQL commands
cursor = conn.cursor()

#create a table
cursor.execute("""CREATE TABLE population 
  (city TEXT, state TEXT, population INT)""")

#close db connection
conn.close()
