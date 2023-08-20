number_rows = int(input())
students = {}

for info in range(number_rows):
    current_student = input()
    current_grade = float(input())
    if current_student not in students:
        students[current_student] = []
    students[current_student].append(current_grade)

students = {student: sum(students[student]) / len(students[student]) for student in students}
students = {student: grade for student, grade in students.items() if grade >= 4.50}
for student, grade in students.items():
    print(f"{student} -> {grade:.2f}")
