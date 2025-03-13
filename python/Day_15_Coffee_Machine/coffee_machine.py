from coffee_data import MENU
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from input_checker import input_in_collection, input_is_int
# variables
money = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coin_types = {
    "quarters" : 0.25,
    "dimes" : 0.1,
    "nickles" : 0.05,
    "pennies" : 0.01,
}

# TODO: Print report.
def report():
    for key, value in resources.items():
        unit = "g" if key=="coffee" else "ml"
        print(f"{key}: {value}{unit}")
    print(f"Money: ${money:.2f}")

# TODO: Turn off the Coffee Machine by entering “ off​ ” to the prompt.
def off():
    machine_status = False
    return 2

# TODO: Process coins.
def cost(coffee_cost):
    total_money_inserted = 0
    for key, value in coin_types.items():
        no_of_coin_inserted = input_is_int(input(f"How many {key}: "))
        total_money_inserted += no_of_coin_inserted * value
        print(total_money_inserted)
    return total_money_inserted - coffee_cost

def coffee(coffee_type):
    global money
    ingredients = MENU[coffee_type]["ingredients"]
# TODO: Check resources sufficient?
    for key, value in ingredients.items():
        if value > resources[key]:
            print(f"Sorry there is not enough {key}")
            return -1
    cost_of_coffee = MENU[coffee_type]["cost"]
    change = cost(cost_of_coffee)
# TODO: Check transaction successful?
    if change < 0:
        print("Sorry thats' not enought money. Money refunded.")
        return -2
    else:
        print(f"Here is ${change:.2f} dollars in change.")
        money += cost_of_coffee
    for key, value in ingredients.items():
        resources[key] -= value
    return 0

def refill():
    resource = input_in_collection(input("What would you like to refill?"), resources)
    quantity = input_is_int(input("How much would you like to add: "))
    resources[resource] += quantity

commands = {
    "report" : report,
    "off" : off,
    "refill" : refill,
    }
coffee_types ={
    "espresso" : coffee,
    "latte" : coffee,
    "cappuccino" : coffee,
}
machine_status = True
while machine_status:

# TODO:  Prompt user by asking “ What would you like? (espresso/latte/cappuccino):​ ”
    command = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
    if command in commands:
        status_code = commands[command]()
        if status_code == 2: break
    elif command in coffee_types:
        status_code = coffee_types[command](command)
        if status_code < 0: continue
# TODO: Make Coffee.
        else: print(f"Here is your latte. Enjoy your {command}. 🍵")
    else: print("Invalid command!!!")

print("Machine off!!!")
