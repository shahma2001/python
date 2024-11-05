# Function to calculate factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact

# Function to calculate the sum of the series
def series_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += (i ** i) / factorial(i)
    return total

# Input from user
n = int(input("Enter the value of n: "))

# Calculate the sum
result = series_sum(n)

# Output the result
print(f"The sum of the series up to {n} terms is: {result}")


