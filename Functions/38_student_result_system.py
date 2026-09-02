"""
Q38. Student Result System

Modular grading system with functions for:
- calculate_total(marks)
- calculate_percentage(total, num_subjects)
- calculate_grade(percentage)
"""

def calculate_total(marks):
    return sum(marks)

def calculate_percentage(total, number_of_subjects):
    return total / number_of_subjects

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

marks = [86, 74, 78, 92, 88]
total = calculate_total(marks)
percentage = calculate_percentage(total, len(marks))
grade = calculate_grade(percentage)

print("=" * 10, "RESULT", "=" * 10)
print(f"Total:      {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade:      {grade}")
print("=" * 28)
