
import random

def get_random_python_code():
    """Generate a random Python code snippet."""
    # Randomly select a Python keyword
    keywords = ["if", "else", "while", "for", "def"]
    keyword = random.choice(keywords)

    # Randomly select a variable name
    variables = ["x", "y", "z", "a", "b"]
    variable = random.choice(variables)

    # Randomly select an operation
    operations = ["+", "-", "*", "/"]
    operation = random.choice(operations)

    # Generate the code snippet
    return f"{keyword} {variable} {operation} {random.randint(1, 10)}:"