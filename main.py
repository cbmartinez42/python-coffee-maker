# from dict import MENU, resources
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def money_handler():
    quarters = int(input("Enter number of quarters: ")) * .25
    dimes = int(input("Enter number of dimes: ")) * .10
    nickels = int(input("Enter number of nickels: ")) * .05
    pennies = int(input("Enter number of pennies: ")) * .01
    deposited = quarters + dimes + nickels + pennies
    if deposited < price:
        print(f"You have deposited {deposited}. That is not enough. ")
        money_handler()
    else:
        change = deposited - price
        make_coffee()
        if change > 0:
            make_change()
        

def make_coffee():
    check_ingredients()

    
def check_ingredients():
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
    print("make_change fired")
    
    
# def init():
ingredient_list = []
order = input("What would you like? (espresso, latte, cappuccino): ")
price = MENU[order]["cost"]
print(f"The price for that item is {price}. Please insert your coins:\n")
money_handler()

# init()
