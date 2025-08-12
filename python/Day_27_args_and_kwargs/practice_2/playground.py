import math

def calculate(n, **kwargs):
    n /= kwargs.get("divide", 1)
    n += kwargs.get("add", 0)
    n *= kwargs.get("multiply", 1)
    n -= kwargs.get("subtract", 0)
    return n

print(calculate(1, add = 2))
