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

        try:
            num1 = float(input("\nWhat's the first number?: "))
        except ValueError:
            print("Invalid Input!!!\n\nTry Again!!!")
            continue

    else:
        break
    print("\n+\n-\n*\n/")

    operator = input("\nPick an operation: ")
    if operator not in "+-*/":
        print("\nInvalid Operator!!!\n\nTry Again!!")
        continue
    try:
        num2 = float(input("\nWhat's the next number?: "))
    except ValueError:
        print("Invalid Input!!!\n\nTry Again!!!")
        continue

    calculation=cal(num1, num2, operator)

    result = calculation.operator_selector()

    print(f"\n{num1} {operator} {num2} = {result}")

    continuation = input(f"\nType 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
