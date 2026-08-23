'''Simple Interest
Take:

Principal
Rate
Time

Calculate simple interest.

Formula:

SI = (P × R × T) / 100'''

principle = float(input("Enter the principle Amount:"))
rate = float(input("Enter the rate Amount:"))
time = int(input("Enter the time in months:"))

Si=(principle*rate*time)/100

print("Simple Interest =",Si)