import random

def get_random_code():
    """Generate a random code"""
    code = ""
    for i in range(12):
        code += str(random.randint(0, 9))
    return code