from dict import MENU, resources
# order = str
# price = float


def money_handler():
    """Handles taking money """
    total = int(input("Enter number of quarters: ")) * .25
    total += int(input("Enter number of dimes: ")) * .10
    total += int(input("Enter number of nickels: ")) * .05
    total += int(input("Enter number of pennies: ")) * .01

    if total < float(price):
        print(f"You have deposited {total}. That is not enough. ")
        money_handler()
    else:
        change = total - price
        make_coffee()
        if change > 0:
            make_change()
        

def make_coffee():
    """Overall function for making coffee"""
    check_ingredients()

    
def check_ingredients():
    """Standalone function to check for ingredients"""
    for ingredient in MENU[order]["ingredients"]:
        resource_qty = resources.get(ingredient)
        order_qty = MENU[order]["ingredients"].get(ingredient)
        if resource_qty < order_qty:
            print(f"We are all out of {ingredient}. Try again tomorrow, sucker. Quitting")
            exit(42)
        else:
            # remainder = resource_qty - order_qty
            # print("remainder is> ", remainder)
            resources[ingredient] = resource_qty - order_qty
        ingredient_list.append(ingredient)
    print(resources)
    
    
def make_change():
    """Handles making change"""
    print("make_change fired")
    
    
# def init():
ingredient_list = []
order = input("What would you like? (espresso, latte, cappuccino): ")
if order == "resources":
    for item in resources:
        print(resources)
        # init()
price = MENU[order]["cost"]
print(f"The price for that item is {price}. Please insert your coins:\n")
money_handler()

# init()
