'''Q9. Grade Calculator

Take marks from the user:
90–100 -> A
80–89  -> B
70–79  -> C
60–69  -> D
Below 60 -> F'''

marks = int(input("Enter the marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")
