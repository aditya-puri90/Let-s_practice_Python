"""
Q12. Temperature Converter

Create celsius_to_fahrenheit(celsius) that returns Fahrenheit:
F = (C * 9/5) + 32
"""

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

temp_c = 35
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")
