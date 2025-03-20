import random

def generate_random_code():
    """
    Generates a random 8-digit code using the ASCII character set.
    """
    code = ""
    for i in range(8):
        code += chr(random.randint(65, 90))
    return code