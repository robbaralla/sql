#insert data
import sqlite3

#create connection
conn = sqlite3.connect("new.db")

cursor = conn.cursor()

#insert shit
cursor.execute("UPDATE population SET city = 'AMSTERDAM CITY'\
 WHERE city = 'NEW AMSTERDAM CITY'")

conn.commit()

conn.close() 