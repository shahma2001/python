
color_list1=input("enter the color for list1:").split()
color_list2=input("enter the colors for list2:").split()
color_list3=[color for color in
        color_list1 if color not in
        color_list2]
print("color in list 1 but not in list2:",color_list3)
