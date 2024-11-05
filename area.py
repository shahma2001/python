# Area of square
area_square = lambda side: side ** 2

# Area of rectangle
area_rectangle = lambda length, width: length * width

# Area of triangle
area_triangle = lambda base, height: 0.5 * base * height
# Example of square
side = 4
print("Area of square:", area_square(side))  # Output: 16

# Example of rectangle
length = 5
width = 3
print("Area of rectangle:", area_rectangle(length, width))  # Output: 15

# Example of triangle
base = 6
height = 8
print("Area of triangle:", area_triangle(base, height))  # Output: 24


