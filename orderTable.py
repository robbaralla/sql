import sqlite3

with sqlite3.connect("cars.db") as connection:
    c=connection.cursor()

    #c.execute("CREATE TABLE orders(make TEXT, model TEXT, order_date DATE)")

    cars = [
        ('Honda', 'accord', '1989-12-28'),
        ('Honda', 'accord', '1989-12-27'),
        ('Honda', 'accord', '1989-12-26'),
        ('Ford', 'FOCUS', '1989-12-28'),
        ('Ford', 'FOCUS', '1989-12-27'),
        ('Ford', 'FOCUS', '1989-12-26'),
        ('Honda', 'delta', '1988-10-26'),
        ('Honda', 'delta', '1988-10-25'),
        ('Honda', 'delta', '1988-10-24'),
        ('Ford', 'MONDEO', '1987-12-26'),
        ('Ford', 'MONDEO', '1987-12-26'),
        ('Ford', 'MONDEO', '1987-12-26'),
        ('Honda', 'trx', '1908-01-26'),
        ('Honda', 'trx', '1908-04-26'),
        ('Honda', 'trx', '1908-05-26')
    ]

    c.executemany("INSERT INTO orders VALUES(?,?,?)", cars)

    c.execute("SELECT * FROM orders order by make ASC")

    #c.execute("SELECT DISTINCT  inventory.make, inventory.model, orders.order_date \
     # FROM inventory, orders WHERE orders.make =  inventory.make && orders.model = \
      #inventory.model")


    rows = c.fetchall()

    for r in rows:
      print ("make: " + r[0] + " model: " + r[1] + " order date: " + r[2])
      print ("")