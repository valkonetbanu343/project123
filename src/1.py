import random

def get_random_code():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    code = ""
    for i in range(10):
        code += random.choice(numbers) + random.choice(letters)
    return code