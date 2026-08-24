'''Rectangle Calculator

Take length and width and calculate:

Area
Perimeter

Also print the results neatly.

Formula:

Area = length × width
Perimeter = 2 × (length + width)'''

length = int(input("Enter the length:"))
width = int(input("Enter the width:"))

print("Area :",length * width)
print("Perimeter :",2*(length + width))