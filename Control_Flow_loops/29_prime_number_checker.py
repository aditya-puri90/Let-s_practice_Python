'''Q29. Prime Number

Take a number and determine whether it is prime.'''

num = int(input("Enter number: "))

if num < 2:
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a Prime Number.")
    else:
        print(f"{num} is not a prime number.")
