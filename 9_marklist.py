# 9 Student Performance Analysis System

def total_marks(marks):
    return sum(marks)

def find_avg(marks):
    return sum(marks) / len(marks) if marks else 0         #ternary operator (Python's short inline if-else statement) to prevent a program crash caused by dividing by zero.

def find_highest(marks):
    return max(marks) if marks else 0

def find_lowest(marks):
    return min(marks) if marks else 0

def find_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"

num_students = int(input("Enter number of students: "))
students = []

for _ in range(num_students):
    name = input("\nEnter student name: ")
    marks_input = input("Enter marks separated by space: ")
    marks = [int(m) for m in marks_input.split()]

    total = total_marks(marks)
    avg = find_avg(marks)
    high = find_highest(marks)
    low = find_lowest(marks)
    grade = find_grade(avg)

    students.append({
        "name": name,
        "marks": marks,
        "total": total,
        "average": avg,
        "highest": high,
        "lowest": low,
        "grade": grade
    })

print("\nStudent Performance Analysis")
for s in students:
    print(f"Name: {s['name']} | Marks: {s['marks']} | Total: {s['total']} | Avg: {s['average']:.2f} | High: {s['highest']} | Low: {s['lowest']} | Grade: {s['grade']}")

# Sort students using a lambda expression based on total marks (descending)
sorted_students = sorted(students, key=lambda s: s["total"], reverse=True)

print("\nStudents Sorted by Total Marks")
for s in sorted_students:
    print(f"Name: {s['name']} - Total Marks: {s['total']}")