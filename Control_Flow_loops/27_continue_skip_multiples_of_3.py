'''Q27. Skip Multiples of 3

Print numbers from 1 to 20, but skip numbers divisible by 3 using continue.'''

for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)
