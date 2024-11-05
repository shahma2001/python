def add_numbers(*args):
    """
    This function takes a variable number of integer arguments and returns their sum.

    Parameters:
    *args (int): A variable number of integer arguments.

    Returns:
    int: The sum of the given integers.

    Example:
    >>> add_numbers(1, 2, 3)
    6

    >>> add_numbers(5, 10, 15, 20)
    50
    """
    # Initialize sum to 0
    total = 0

    # Iterate through all arguments and sum them
    for num in args:
        total += num

    return total


# Example usage:
print(add_numbers(1, 2, 3))       # Output: 6
print(add_numbers(5, 10, 15, 20)) # Output: 50
print(add_numbers(10))            # Output: 10
print(add_numbers())              # Output: 0


