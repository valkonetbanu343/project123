import random

def get_random_code(length):
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    code = ""
    for i in range(length):
        if i % 2 == 0:
            code += random.choice(letters)
        else:
            code += random.choice(numbers)
    return code
