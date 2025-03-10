import random
import string
def get_random_code(length):
    letters = string.ascii_letters
    numbers = string.digits
    code = ""
    for i in range(length):
        code += random.choice(letters)
        code += random.choice(numbers)
    return code