"""
Pizza Time
Description: Manages pizza orders, checkout, and inventory for a pizzaria.
Author: Agile
"""

import order, checkout, inventory


print("Welcome to Pizza Time!\n\nSelect an option Below\n\n\n1. Order\n2. Checkout\n3. Inventory\n4. Exit the program\n\n")

while True:
    try:
        selection = int(input(">> "))
        if selection == 1 or selection == 2 or selection == 3 or selection == 4:
            if selection == 1:
                order.start()
            elif selection == 2:
                checkout.start()
            elif selection == 3:
                inventory.start()
            else:
                print("Goodbye")
                break

        else: 
            print("Please select 1, 2, 3, or 4.")
    except:
        print("Please select 1, 2, 3, or 4.")

