# Function to check if a number is Armstrong
def is_armstrong(number):
    digits = [int(digit) for digit in str(number)]
    num_digits = len(digits)
    sum_of_powers = sum(digit ** num_digits for digit in digits)
    return sum_of_powers == number

# Function to generate Armstrong numbers between two limits
def generate_armstrong_numbers(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

# Define the range
start_limit = int(input("Enter the starting limit: "))
end_limit = int(input("Enter the ending limit: "))

# Generate and print Armstrong numbers
armstrong_numbers = generate_armstrong_numbers(start_limit, end_limit)
print(f"Armstrong numbers between {start_limit} and {end_limit}: {armstrong_numbers}")


