x=list(map(int,input("enter list1").split()))
y=list(map(int,input("enter list2").split()))
same= set(x) & set(y)
length= len(x) == len(y)
if(sum(x) == sum(y)):
    print("sum is same")
else:
    print("Sum is not same")
print("common elements is :",same)
if (length == True):
    print("same length")
else:
    print("not same length")
 

