#create a car database

import sqlite3
#connect to the db
conn=sqlite3.connect("cars.db")

#get a cursor
cursor = conn.cursor()

cursor.execute("""CREATE TABLE inventory( make TEXT, model TEXT, quantity INT)""")


#close conection
conn.close()