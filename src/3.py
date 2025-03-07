import random

def get_random_python_code():
    # Generate a random number between 1 and 10
    num = random.randint(1, 10)

    # Return a string based on the random number
    if num == 1:
        return "print('Hello World!')"
    elif num == 2:
        return "print('The answer to life is', 42)"
    elif num == 3:
        return "print('The meaning of life is', 'not easy')"
    elif num == 4:
        return "print('I am a random string')"
    elif num == 5:
        return "print('A', 'random', 'string')"
    elif num == 6:
        return "print('Random', 'string')"
    elif num == 7:
        return "print('A random string with', 'variables')"
    elif num == 8:
        return "print('A random string with', 'a mix of variables', 'and a function call')"
    else:
        return "print('A random string with', 'a mix of variables', 'and a function call', 'with a list comprehension')"