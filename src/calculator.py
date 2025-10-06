"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""

def add(a, b):
    """Add two numbers together"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers """
    # input validation: both arguments must be numbers
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a * b

def divide(a, b):
    """Divide a by b """
    # validate inputs are numeric
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    # division by zero
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
    

# TODO: Students will add multiply, divide, power, sqrt functions

if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")