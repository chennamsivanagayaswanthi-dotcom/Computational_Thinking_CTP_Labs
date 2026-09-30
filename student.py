from typing import Dict


def calculate_result(
    name: str,
    mark1: float,
    mark2: float,
    mark3: float
) -> Dict[str, float | str]:

    marks = [mark1, mark2, mark3]

    # Validate marks
    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Marks must be between 0 and 100")

    total = sum(marks)
    average = total / 3

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    return {
        "name": name,
        "total": total,
        "average": average,
        "grade": grade
    }


result = calculate_result("Yaswanthi", 80, 90, 70)

print("Student:", result["name"])
print("Total:", result["total"])
print("Average:", result["average"])
print("Grade:", result["grade"])