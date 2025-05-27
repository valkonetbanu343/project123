import random

def generate_random_string(length):
    """Generate a random string of given length."""
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

# Generate a random string of 10 characters
random_str = generate_random_string(10)
print(random_str)
