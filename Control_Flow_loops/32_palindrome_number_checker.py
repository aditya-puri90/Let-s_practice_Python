'''Q32. Palindrome Number

Check whether a number reads the same forward and backward.'''

num = int(input("Enter number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print(f"{original} -> Palindrome")
else:
    print(f"{original} -> Not Palindrome")
