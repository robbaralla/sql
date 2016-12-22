#delete and update
import sqlite3

#get connection
with sqlite3.connect("cars.db") as connection:
  c = connection.cursor()

  # insert
  c.execute("INSERT INTO inventory VALUES('Honda', 'trx',\
    25)")
  c.execute("INSERT INTO inventory VALUES('Honda', 'accord',\
    2)")
  c.execute("INSERT INTO inventory VALUES('Honda', 'delta',\
    22)")
  c.execute("INSERT INTO inventory VALUES('FORD', 'FOCUS',\
    20)")
  c.execute("INSERT INTO inventory VALUES('FORD', 'MONDEO',\
    25)")

    
  print ("\nNEW Data:\n")
  c.execute("SELECT * from inventory")
  result = c.fetchall()

  for r in result:
    print (r[0], r[1], r[2])

  # update
  c.execute("UPDATE inventory SET quantity=9000000 where\
  model='FOCUS'")

  print ("\nFORD!!:\n")
  c.execute("SELECT * from inventory where make='FORD' ")
  result = c.fetchall()

  for r in result:
    print (r[0], r[1], r[2])
