def is_armstrong(number):
    # Convert the number to a string to easily iterate over its digits
    digits = str(number)
    num_digits = len(digits)

    # Calculate the sum of each digit raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)

    # Check if the sum is equal to the original number
    return sum_of_powers == number

# Example usage:
if __name__ == "__main__":
    # Test the function with some examples
    test_numbers = [153, 9474, 370, 371, 123]
    for num in test_numbers:
        print(f"{num} is an Armstrong number: {is_armstrong(num)}")

