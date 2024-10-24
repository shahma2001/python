integers=[int(x) for x in input("enter a list of integers(space-separated):").split()]
word = input("enter a word:")
postive_numbers=[num for num in integers if num>0]
squared_numbers=[num** 2 for num in integers]
vowels=[char for char in word if char in'aeiouAEIOU']
ordinal_values=[ord(char) for char in word]
print("\n(a) positive numbers from the list:",postive_numbers)
print("(b) sqaures of the numbers:", squared_numbers)
print("(c) ordinal value of each character in the word:",ordinal_values)
