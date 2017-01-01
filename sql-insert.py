import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
    c=connection.cursor()
    #if sucha table exists, drop it
    c.execute("DROP TABLE if exists numbers")
    #now create it
    c.execute("CREATE TABLE numbers (num INT)")

    #insert 100 random numbers
    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)", (random.randint(0,100),))


