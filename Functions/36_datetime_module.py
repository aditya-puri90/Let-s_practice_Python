"""
Q36. Python Datetime Module

Demonstrates retrieving current system date and time using datetime.
"""

import datetime

now = datetime.datetime.now()
print("Current Date & Time:", now)
print("Current Date:       ", now.strftime("%Y-%m-%d"))
print("Current Time:       ", now.strftime("%H:%M:%S"))
