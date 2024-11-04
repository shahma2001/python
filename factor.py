def factors(num):
    factor_list= []
    i = 1
    while i <= num:
        if num % i ==0:
           factor_list.append(i)
        i += 1
    return factor_list
num = int(input("Enter a number to find its factors:"))
print(f"Factors of {num}: {factors(num)}")
