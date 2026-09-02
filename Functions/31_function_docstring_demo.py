"""
Q31. Function Docstring

Create area_of_rectangle(length, width) with docstrings detailing parameters and return values.
Access docstring via __doc__.
"""

def area_of_rectangle(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
    length (float/int): Length of the rectangle.
    width (float/int): Width of the rectangle.

    Returns:
    float/int: Area calculated as length * width.
    """
    return length * width

print("Area:", area_of_rectangle(10, 5))
print("\nFunction Docstring:")
print(area_of_rectangle.__doc__)
