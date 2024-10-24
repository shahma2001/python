n= int(input("enter the number of items in the dictionary:"))
dictionary={}
for _ in range(n):
    key=input("enter key :")
    dictionary[key]=value
ascending=dict(sorted(dictionary.items(),key=lambda item:item[1]))
descending=dict(sorted(dictionary.items(),key=lambda item:item[1], reverse=true))
    print("ascending:",ascending)
    print("descending:", descending)
