import coffee_data
import coffee_functions
from input_checker import input_in_collection

# variables
resources = coffee_data.resources

money = 0
machine_on = coffee_functions.machine_status = True
commands = coffee_functions.list_of_commands
coffee_types = coffee_functions.list_of_coffee_types

while machine_on:

# Prompt user by asking “ What would you like? (espresso/latte/cappuccino):​ ”
    command = input_in_collection(input("What would you like? (espresso/latte/cappuccino): ").strip().lower(), commands | coffee_types)
    if command in commands:
        if command == "report":
            commands[command](resources, money)
        elif command == "off":
            break
        else:
            commands[command](resources)
    elif command in coffee_types:
        cost_update = coffee_types[command](command, resources)
        if cost_update < 0: continue
        else:
            money += cost_update
            print(f"Here is your latte. Enjoy your {command}. 🍵")
    else: print("Invalid command!!!")

print("Machine off!!!")
