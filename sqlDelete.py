#delete and update
import sqlite3

#get connection
with sqlite3.connect("new.db") as connection:
  c = connection.cursor()

  # delete
  c.execute("DELETE from population where city='NEW YORK CITY'")
  
  # update
  c.execute("UPDATE population SET population=9000000 where\
   city='AMSTERDAM CITY'")
  
  print ("\nNEW Data:\n")
  c.execute("SELECT * from population")
  result = c.fetchall()

  for r in result:
    print (r[0], r[1], r[2]) 