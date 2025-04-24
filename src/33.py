import random

def generate_random_string(length):
    """
    Generate a random string of specified length.
    
    Args:
        length (int): The desired length of the generated string.
        
    Returns:
        str: A randomly generated string of the given length.
    """
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length))

random_string = generate_random_string(10)
print(random_string)
