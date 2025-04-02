import random

def generate_random_string(length):
    """
    Generate a random string of specified length.
    
    Args:
        length (int): The length of the generated string.
        
    Returns:
        str: A randomly generated string.
    """
    # Ensure length is positive and at least 10 characters long
    if length < 10 or length > 256:
        raise ValueError("Length must be between 10 and 256")
    
    # Generate a random ASCII string of the specified length
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length))

# Example usage:
random_string = generate_random_string(10)
print(random_string)
