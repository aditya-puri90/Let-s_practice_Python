"""
Q8. Convert Celsius to Fahrenheit

Given:
    celsius = [0, 10, 20, 30, 40]
Use map() to convert every value to Fahrenheit.
Formula:
    F = (C * 9/5) + 32
"""

celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9 / 5) + 32, celsius))

if __name__ == "__main__":
    print("Celsius temperatures:", celsius)
    print("Fahrenheit temperatures:", fahrenheit)
