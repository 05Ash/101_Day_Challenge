class Calculator:
    def __init__(self, num1, num2, sign):
        self.num1 = num1
        self.num2 = num2
        self.sign = sign


    def operator_selector(self):
        #print(self.num1)
        def add(self): return self.num1 + self.num2
        def subtract(self): return self.num1 - self.num2
        def multiply(self): return self.num1 * self.num2
        def divide(self):
            try:
                return self.num1 / self.num2
            except ZeroDivisionError:
                print("Invalid input, not divisible by zero.")

        operations = {
            "+" : add,
            "-" : subtract,
            "*" : multiply,
            "/" : divide,
        }

        return operations[self.sign](self)
