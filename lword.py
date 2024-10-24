
words=input("enter the list of word separated by spaces:").split()
max_length=0
for word in words:
    if len(word)>max_length:
        max_length=len(word)
        longest=word
        print("the length of the longest word is:",max_length)
        print("the word is:",longest)
