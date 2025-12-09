"""
Main application module containing core business logic.
"""


def add_numbers(a, b):
    """
    Add two numbers together.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
    
    Returns:
        Sum of a and b
    
    Raises:
        TypeError: If inputs are not numeric
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numeric (int or float)")
    
    return a + b
