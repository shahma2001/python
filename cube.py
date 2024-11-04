def is_armstrong(num):
    sum_of_cubes = 0
    temp = num
    num_digits = len(str(num))
    while temp > 0:
        digit = temp % 10
        sum_of_cubes += digit ** num_digits
        temp //=10
    return sum_of_cubes == num
num = int(input("Enter a number: "))
if is_armstrong(num):
   print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
