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


def init():
    order = input("What would you like? (espresso, latte, cappuccino): ")
    price = MENU[order]["cost"]
    print(f"The price for that item is {price}. Please insert your coins:")
    money_handler(price)


def money_handler(price):
    quarters = int(input("Enter number of quarters: ")) * .25
    dimes = int(input("Enter number of dimes: ")) * .10
    nickels = int(input("Enter number of nickels: ")) * .05
    pennies = int(input("Enter number of pennies: ")) * .01
    entered = quarters + dimes + nickels + pennies


init()
