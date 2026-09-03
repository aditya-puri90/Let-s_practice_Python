'''
Q8. Count even numbers

Given:

numbers = [10, 15, 22, 33, 40, 51, 60]

Count how many numbers are even.
'''

numbers = [10, 15, 22, 33, 40, 51, 60]
count =0
for num in numbers:
    if num % 2 ==0:
        count +=1
        print("Even Number:",count)