import printslow

# Needs total price w/ tax, Give change

def start(customer_order):
    printslow.slow_type("This is the checkout system\n\n")
    subtotal = 0
    tax_rate = 0.095
    for i in customer_order:
        print(i.quantity, i.size, i.type, i.price)
        subtotal += i.quantity * i.price
    
    subtotal = round(subtotal, 2)
    tax = round(subtotal * tax_rate, 2)
    total = round(subtotal + tax, 2)

    printslow.slow_type(f"Subtotal: ${subtotal}")
    printslow.slow_type(f"Tax: ${tax}")
    printslow.slow_type(f"Total: ${total}")

    payment(total)

    save(customer_order, total)

    input("\n\nPress Enter to continue.\n\n\n")

def payment(total):

    change = 0
    
    while True:
            if total < 500:
                payment_type = input("Cash or credit?: \n\n>>")

                if payment_type.lower() == "cash":
                    printslow.slow_type(f"The total is ${total}")
                    try:
                        cash = float(input("Provide cash for purchase.\n\n>>"))
                    except:
                        printslow.slow_type("Please provide a number")
                        continue
                    
                    change = round(cash - total, 2)

                    print(f"Return ${change} to the customer.")
                    input("press enter to continue")
                    break

                elif payment_type.lower() == "credit":
                    input(f"The total is ${total}\nPlease swipe the credit card.\n\nPress ENTER after completing the credit card transaction.")
                    break

                else:
                    printslow.slow_type("Please enter cash or credit only.")
            elif total >= 500:
                 printslow.slow_type("\n\nUnfortunately, company policy prevents us from accepting cash for orders larger than $500. Please provide credit information.\n\n")
                 input(f"The total is ${total}\nPlease swipe the credit card.\n\nPress ENTER after completing the credit card transaction.")
                 break


def save(order, total):
    with open("pizza.dat", "a") as orders:
        for i in order:
            orders.write(f"{i.quantity}, {i.size}, {i.type}, ${i.price}, ")
        orders.write(f"${total}\n")










"""
    while True:
        for i in customer_order:
            print(i.quantity, i.size, i.type, i.price)

        printslow.slow_type("\n\n Is this your order? (y)es or (n)o \n\n")

        answer = input(">> ")

        if answer.lower() == "y":
            printslow.slow_type("\nGood! Here you go!")
            break
        elif answer.lower() == "n":
            printslow.slow_type("\nPlease go back to the order menu to fix your order.")
            break
        else:
            printslow.slow_type("\nPlease input either y for yes or n for no.\n\n\n")
            continue
"""