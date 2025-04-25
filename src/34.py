import random

def create_random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''.join(random.sample(letters, length))
    return result

random_string = create_random_string(10)
print(random_string)
