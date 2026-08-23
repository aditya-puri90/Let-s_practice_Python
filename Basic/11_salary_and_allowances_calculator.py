'''Salary Calculator

Take basic salary as input.

Calculate:

HRA = 20% of salary
DA = 10% of salary
Total Salary = Salary + HRA + DA'''

salary = int(input("Enter the salary:"))
Hra = salary * 20 /100
Da = salary * 10/100
total_sal = salary + Hra + Da

print("HRA =",Hra,"DA =", Da,"Total salary =",total_sal)