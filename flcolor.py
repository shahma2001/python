color_list1=input("enter color for color_list1(separated by space):").split()
color_list2=input("enter color for color_list2(separated by space):").split()
color_list3=[color for color in color_list1 if color not in color_list2]
print("color in list 1 but not in list 2:",color_list3)




