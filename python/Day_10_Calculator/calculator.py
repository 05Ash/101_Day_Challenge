class Calculator:
    def __init__(self, num1, num2, sign):
        self.num1 = num1
        self.num2 = num2
        self.sign = sign


    def operator_selector(self):

        if self.sign == "+":
            return self.num1 + self.num2
        if self.sign == "-":
            return self.num1 - self.num2
        if self.sign == "*":
            return self.num1 * self.num2
        if self.sign == "/":
            try:
                return self.num1 / self.num2
            except ZeroDivisionError:
                print("Invalid input, not divisible by zero.")
