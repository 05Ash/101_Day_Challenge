from coffee_data import MENU, coin_types
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from input_checker import input_in_collection, input_is_int

def report(resources, money):
    """Take resources(dict) and money as argument, and print them one by one"""
    for key, value in resources.items():
        unit = "g" if key=="coffee" else "ml"
        print(f"{key}: {value}{unit}")
    print(f"Money: ${money:.2f}")

def off():
    """use a global variable and change it to false"""
    global machine_status
    machine_status = False
    return 2

def cost(coffee_cost):
    """Take the cost of coffee and currency_types as an argument and return the extra value"""
    total_money_inserted = 0
    for key, value in coin_types.items():
        no_of_coin_inserted = input_is_int(input(f"How many {key}: "))
        total_money_inserted += no_of_coin_inserted * value
    return total_money_inserted - coffee_cost

def make_coffee(coffee_type, resources):
    """Make a given coffee and check if the resources and coins provided are enough"""
    ingredients = MENU[coffee_type]["ingredients"]
# Check resources sufficient?
    for key, value in ingredients.items():
        if value > resources[key]:
            print(f"Sorry there is not enough {key}")
            return -1
    cost_of_coffee = MENU[coffee_type]["cost"]
    change = cost(cost_of_coffee)
# Check transaction successful?
    if change < 0:
        print("Sorry thats' not enought money. Money refunded.")
        return -2
    else:
        print(f"Here is ${change:.2f} dollars in change.")
    for key, value in ingredients.items():
        resources[key] -= value
    return cost_of_coffee

def refill(resources):
    """Refill the lacking resources"""
    resource = input_in_collection(input("What would you like to refill?: "), resources)
    quantity = input_is_int(input("How much would you like to add: "))
    resources[resource] += quantity

list_of_commands = {
    "report" : report,
    "off" : off,
    "refill" : refill,
    }
list_of_coffee_types ={
    "espresso" : make_coffee,
    "latte" : make_coffee,
    "cappuccino" : make_coffee,
}
