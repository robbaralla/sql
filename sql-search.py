import sqlite3

with sqlite3.connect("newnum.db") as connection:
    c=connection.cursor()

    prompt= """pick an operation:
            1: average
            2: min
            3: max
            4: sum
            5: exit
            """
    while True:
        #get user input
        x = input(prompt)
        if x == "1":
            operation = "avg"    
        elif x == "2":
            operation = "min"
        elif x == "3":
            operation = "max"
        elif x == "4":
            operation = "sum"
        elif x == "5":
            print("Exit")
            break

        c.execute("SELECT {}(num) FROM numbers".format(operation))

        get = c.fetchone()

        print (operation + " = {}".format(get[0]))
