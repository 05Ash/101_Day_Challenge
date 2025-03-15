from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

myCoffeeMachine = MoneyMachine()
myCoffeeMacker = CoffeeMaker()
myMenu = Menu()

for item in myMenu.menu:
    print(item.name, item.cost, item.ingredients)

machineStatus = True
while machineStatus:
    userChoice = input(f"What would you like {myMenu.get_items()}: ").strip().lower()
    if userChoice == "off":
        break
    elif userChoice == "report":
        print(myCoffeeMacker.report())
        print(myCoffeeMachine.report())
    else:
        userChoice = myMenu.find_drink(userChoice)
        if userChoice != None:
            if myCoffeeMacker.is_resource_sufficient(userChoice):
                if myCoffeeMachine.make_payment(userChoice.cost):
                    myCoffeeMacker.make_coffee(userChoice)
