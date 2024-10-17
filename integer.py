numbers=[int(x) for x in
        input("enter a list of integers(space-separated):").split()]
odd_numbers=[num for num in numbers if num %2 !=0]
print("List after removing even numbers:",odd_numbers)
