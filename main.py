from dict import MENU, resources


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
    ingredient_list = []
    for ingredient in MENU[order]["ingredients"]:
        if resources.get(ingredient) < MENU[order]["ingredients"].get(ingredient):
            print(f"We are all out of {ingredient}. Try again tomorrow, sucker. Quitting")
            exit(42)
        ingredient_list.append(ingredient)
    print(ingredient_list)
    
    
def make_change():
    print("make_change fired")
    
    
# def init():
order = input("What would you like? (espresso, latte, cappuccino): ")
price = MENU[order]["cost"]
print(f"The price for that item is {price}. Please insert your coins:\n")
money_handler()

# init()
