from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

myCoffeeMachine = MoneyMachine()
myCoffeeMacker = CoffeeMaker()
myMenu = Menu()

machineStatus = True
while machineStatus:
    userChoice = input(f"What would you like {myMenu.get_items()}: ").strip().lower()
    if userChoice == "off":
        machineStatus = False
    elif userChoice == "report":
        myCoffeeMacker.report()
        myCoffeeMachine.report()
    else:
        userChoice = myMenu.find_drink(userChoice)
        if userChoice != None and myCoffeeMacker.is_resource_sufficient(userChoice) and myCoffeeMachine.make_payment(userChoice.cost):
            myCoffeeMacker.make_coffee(userChoice)
