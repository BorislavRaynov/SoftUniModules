number_of_students = int(input())
student_records = {}

for student in range(number_of_students):
    name, grade = input().split()
    if name not in student_records:
        student_records[name] = []
    student_records[name].append(float(grade))

for names, grades in student_records.items():
    grade_list = " ".join(str(f"{grade:.2f}") for grade in grades)
    avr_grade = sum(grades) / len(grades)
    print(f"{names} -> {grade_list} (avg: {avr_grade:.2f})")
