# Ask user to input the length of the 3 sides of a triangle
x =float(input("enter the first side: "))
y =float(input("enter the second side: "))
z =float(input("enter the third side: "))
# if all sides are equal print Equilateral
if x == y and y == z:
    print("this is  equialateral")
# if 2 sides are equal print Isosceles
elif x ==y or y == z or x == z:
    print("this is an Isosceles")
# if no sides are equal print Scalene
else:
    print("this is a Scalene")