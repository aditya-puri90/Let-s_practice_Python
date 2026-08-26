'''Q19. Count Numbers

Take a number N and count how many numbers between 1 and N are divisible by 3.'''

N = int(input("Enter N: "))
count = 0

for i in range(1, N + 1):
    if i % 3 == 0:
        count += 1

print("Count =", count)
