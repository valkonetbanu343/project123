
import random

def get_random_code():
    numbers = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyz"
    characters = numbers + letters
    code = ""
    for i in range(12):
        code += random.choice(characters)
    return code