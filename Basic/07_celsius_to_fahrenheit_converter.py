'''Take temperature in Celsius and convert it to Fahrenheit.

Formula:

F = (C × 9/5) + 32'''

temp = float(input("Enter the temperature in celsius:"))
temp_f = (temp * 9/5) +32

print("Temperature in  Fahrenheit =", temp_f)