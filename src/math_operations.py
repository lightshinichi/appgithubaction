def add(A,B):
    """Returns the sum of A and B."""
    return A + B
def subtract(A,B):
    """Returns the difference of A and B."""
    return A - B
def multiply(A,B):
    """Returns the product of A and B."""
    return A * B
def divide(A,B):
    """Returns the quotient of A and B."""
    if B == 0:
        raise ValueError("Cannot divide by zero.")
    return A / B