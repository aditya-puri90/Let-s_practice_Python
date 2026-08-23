'''BMI Calculator

Take:

Weight in kg
Height in meters

Calculate:

BMI = weight / height²'''

weigth = int(input("Enter the Weight in KG:"))
height = int(input("ENter the height in meter:"))

BMI = weigth / height**2

print("BMI =", BMI)