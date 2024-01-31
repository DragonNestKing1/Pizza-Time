"""
Title: Pizza Time
Description: Manages pizza orders, checkout, and inventory for a local pizza store
Author: Alexander Langston
Version: 1.0
"""
import order, checkout, printslow
from os import system

customer_order = []
while True:
    system("cls")
    printslow.slow_type("Welcome to Pizza Time!\n\nSelect an option below.\n\n1. Order\n2. Checkout\n3. Exit\n\n")
    selection = input(">> ")
    if selection == "1":
        customer_order = order.start()
    elif selection == "2":
        if len(customer_order) > 0:
            checkout.start(customer_order)
        else:
            printslow.slow_type("The cart is empty. Please run the order program first.\n\n")
    elif selection == "3":
        printslow.slow_type("Goodbye")
        break
    else:
        printslow.slow_type("Please select one of the given options")
        input("Press Enter to continue.\n\n")