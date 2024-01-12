"""
Pizza Time Order
description: This file is for the ordering system
Author: Agile
"""
# Bug is sending the system back to main, test code in main to see if it will work outside file.
def start():
    print("This is the pizza ordering system")

    while True:
        alltopping = ""
        numpizza = int(input("How many pizzas do you need?\n\n>> "))
        numtopping = int(input("How many toppings?\n\n>>test "))
        while numtopping > 0:
            topping = ("what is one topping you want?\n\n>> ")
            alltopping == (alltopping + f"{topping}, ")
            numtopping -- 1
        print(alltopping)
        break