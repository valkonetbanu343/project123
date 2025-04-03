import math

def square_root(number):
    if number < 0:
        raise ValueError("Square root of a negative number is not defined.")
    
    return math.sqrt(number)

try:
    print(square_root(-16))
except ValueError as e:
    print(e)
