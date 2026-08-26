'''Q10. Number Classification

Take a number and determine whether it is:
- Positive Even
- Positive Odd
- Negative Even
- Negative Odd
- Zero'''

num = int(input("Enter the number: "))

if num > 0 and num % 2 == 0:
    print("Positive Even")
elif num > 0 and num % 2 != 0:
    print("Positive Odd")
elif num < 0 and num % 2 == 0:
    print("Negative Even")
elif num < 0 and num % 2 != 0:
    print("Negative Odd")
else:
    print("Zero")
