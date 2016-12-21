#insert data
import sqlite3

#create connection
conn = sqlite3.connect("new.db")

cursor = conn.cursor()

#insert shit
cursor.execute("INSERT into population VALUES('NEW YORK CITY',\
 'NY', 8000)")
cursor.execute("INSERT into population VALUES('NEW AMSTERDAM CITY',\
 'AN', 8000000)")

conn.commit()

conn.close() 