# utils.py

def calculate_sum(a, b):
    """
    Calculate the sum of two numbers after validating the inputs.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of the inputs.
    """
    # Input validation
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers")

    # Sum calculation
    return a + b

