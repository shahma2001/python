def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
def print_fibonacci_series(n):
    for i in range(n):
        print(fibonacci(i), end=" ")


num_terms = int(input("Enter the number of terms in the Fibonacci series: "))
print_fibonacci_series(num_terms)


