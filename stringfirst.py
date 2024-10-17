input_string=input("enter a string")
if input_string:
    first_char=input_string[0]
    modified_string=first_char + input_string[1:].replace(first_char,'$')
else:
    modified_string=""
print(modified_string)

