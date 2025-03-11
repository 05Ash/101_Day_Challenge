import artwork
from calculator import Calculator as cal

print(artwork.calculator_art)

next_step = True
continuation = "n"
result = None

while next_step:

    if continuation == "y":
        num1 = result

    elif continuation == "n":

        num1 = float(input("\nWhat's the first number?: "))

    else:
        break
    print("\n+\n-\n*\n/")

    operator = input("\nPick an operation: ")
    if operator not in "+-*/":
        print("\nInvalid Operator!!!\n\nTry Again!!")
        continue

    num2 = float(input("\nWhat's the next number?: "))

    calculation=cal(num1, num2, operator)
    result = calculation.operator_selector()

    print(f"\n{num1} {operator} {num2} = {result}")

    continuation = input(f"\nType 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
