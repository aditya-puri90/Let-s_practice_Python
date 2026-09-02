"""
Q37. Third-Party Packages (pip & pyfiglet)

Demonstrates importing and using a third-party package installed via pip.
"""

try:
    import pyfiglet
    text = pyfiglet.figlet_format("Python")
    print(text)
except ImportError:
    print("pyfiglet is not installed. To install run: pip install pyfiglet")
