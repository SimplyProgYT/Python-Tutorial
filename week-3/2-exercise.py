# Area and Perimeter of a Rectangle 

#! Take the length and width from the user

length = float(input("Please enter the length of the rectangle: "))
width = float(input("Please enter the width of the rectangle: "))

#! Calculate the area and perimeter

area = length * width
perimeter = 2 * (length + width)

print("Area: ", area)
print("Perimeter: ", perimeter)