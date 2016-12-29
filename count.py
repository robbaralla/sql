import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT DISTINCT orders.make, orders.model, inventory.quantity FROM orders, inventory\
     WHERE orders.model = inventory.model")
    models = c.fetchall()

    for m in models:
      c.execute("SELECT count(model) FROM orders where model = '{}'".format(m[1]))

      modelCount = c.fetchone()

      c.execute("SELECT sum(quantity) FROM inventory where model = '{}'".format(m[1]))

      carQuantity = c.fetchone()

      print ("car: " + m[0] + " " + m[1] + " has {} orders".format(modelCount))
      print ("quantity: {}".format(carQuantity))