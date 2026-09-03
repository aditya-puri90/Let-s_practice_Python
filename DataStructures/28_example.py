'''
Q28. Count frequency using dictionary ⭐

Given:

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

Create a dictionary showing the frequency of each number.

Expected:

{
    1: 1,
    2: 2,
    3: 3,
    4: 4
}

Hint: Use a loop and dictionary.

'''

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

frequency={}

for num in numbers:
    if num in frequency:
        frequency[num]+=1
    else:
        frequency[num]=1
        print(frequency)