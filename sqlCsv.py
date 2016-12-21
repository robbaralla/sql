#import data from CSV file

import csv
import sqlite3

#conn = sqlite3.connect("new.db")
#c = conn.cursor()
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

#open csv and assign it to a variable
    employees = csv.reader(open("employees.csv", "rU"))
#create new table
#c.execute("CREATE TABLE employees (firstname TEXT, lastname TEXT)")

#insert data
    c.executemany("INSERT INTO employees (firstname, lastname)\
  values (?, ?)", employees)
    c.execute("INSERT INTO employees VALUES('hoi', 'robin')")

#conn.commit()
#conn.close()

