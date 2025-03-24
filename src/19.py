import random

def generate_random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    result_str = ''.join(random.choice(letters) for _ in range(length))
    return result_str

# Example usage:
random_string = generate_random_string(10)
print(random_string)
