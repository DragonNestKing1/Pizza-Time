import printslow, pandas, warnings

class Order:
    def __init__(self, quantity, size, type, price):
        self.quantity = quantity
        self.size = size
        self.type = type
        self.price = float(price[1: ])

warnings.simplefilter(action="ignore", category=FutureWarning)

def start():
    printslow.slow_type("This is the pizza ordering system.\n\n")

    order = []

    while True:
        pizza_menu = pandas.read_csv("data/types.csv")
        pizza_menu = pizza_menu[["Type", "Size", "Price"]]
        print(pizza_menu)
        
        try:
            selection = int(input("\n\nPlease select one of the four options.\n\n>> "))
        except:
            printslow.slow_type("Please select a valid integer\n\n\n")
            continue
       
        if selection > len(pizza_menu) - 1:
            print("please select one of the given options\n\n")
            continue        
        
        size = pizza_menu.iloc[selection][1]
        ptype = pizza_menu.iloc[selection][0]
        price = pizza_menu.iloc[selection][2]
        quantity = int(input(f"\nHow many {size} {ptype} pizzas do you want?  \n\n>> "))

        while True:
            order.append(Order(quantity, size, ptype, price)) # qty, size, ptype, price, total
            printslow.slow_type("Would you like to order another pizza type? (y/n)\n\n")
            confirm = input(">> ")

            if confirm.lower() == "y" or confirm.lower() == "yes" or confirm.lower() == "but wait, theres more":
                continue
            elif confirm.lower() == "n" or confirm.lower() == "no" or confirm.lower() == "hey guys, i guess thats it":
                break
            else:
                printslow.slow_type("\n\nYou need to select one of the options\n\n")

        for i in order:
            print(i.quantity, i.size, i.type, i.price)

        return order