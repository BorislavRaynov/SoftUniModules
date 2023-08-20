import sys

number_students = int(input())
number_lectures = int(input())
bonus = int(input())

maximum_bonus = -sys.maxsize
current_count_student = 0
current_max_student_attendance = 0
current_max_student_bonus = 0

for student in range(1, number_students + 1):
    attendance_student = int(input())
    current_student_bonus = (attendance_student / number_lectures) * (5 + bonus)
    if current_student_bonus > maximum_bonus:
        maximum_bonus = current_student_bonus
        current_max_student_bonus = current_student_bonus
        current_max_student_attendance = attendance_student
        current_count_student = student

print(f"Max Bonus: {round(current_max_student_bonus)}.")
print(f"The student has attended {current_max_student_attendance} lectures.")
