# Define the range of numbers for which we want to calculate powers of 2
n = 10  # Change this value to display more/less powers of 2

# Use map with a lambda function to calculate powers of 2
powers_of_2 = map(lambda x: 2**x, range(n))

# Convert the result to a list and print
print(list(powers_of_2))


