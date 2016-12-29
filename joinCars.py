import sqlite3

with sqlite3.connect("cars.db") as connection:
    c=connection.cursor()

    c.execute("SELECT DISTINCT  inventory.make, inventory.model, inventory.quantity, orders.order_date \
     FROM inventory, orders WHERE inventory.model = orders.model")
    #identical!!!!!!!
    #c.execute("SELECT DISTINCT inventory.make, inventory.model, inventory.quantity, orders.order_date FROM\
    #inventory INNER JOIN orders ON orders.model = inventory.model")


    rows = c.fetchall()

    for r in rows:
      print ("car: " + r[0] + " " + r[1])
      print ("quantity: " + str(r[2]))
      print ("date: " + r[3])
      print ("")