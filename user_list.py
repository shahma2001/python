numbers=("enter a list of numbers").split()
for i in range(len(numbers)):
    if int(numbers[i]) > 100:
        numbers[i]='over'

print(numbers)        
