count_students = int(input())

count_students_level_1 = 0
count_students_level_2 = 0
count_students_level_3 = 0
count_students_level_4 = 0
count_grades = 0
sum_grades = 0

for student in range(1, count_students + 1):
    grade = float(input())
    count_grades += 1
    sum_grades += grade
    if 2.00 <= grade <= 2.99:
        count_students_level_1 += 1
    elif grade <= 3.99:
        count_students_level_2 += 1
    elif grade <= 4.99:
        count_students_level_3 += 1
    elif grade >= 5.00:
        count_students_level_4 += 1

percent_students_level_1 = (count_students_level_1 / count_students) * 100
percent_students_level_2 = (count_students_level_2 / count_students) * 100
percent_students_level_3 = (count_students_level_3 / count_students) * 100
percent_students_level_4 = (count_students_level_4 / count_students) * 100
average_grade = sum_grades / count_grades

print(f"Top students: {percent_students_level_4:.2f}%")
print(f"Between 4.00 and 4.99: {percent_students_level_3:.2f}%")
print(f"Between 3.00 and 3.99: {percent_students_level_2:.2f}%")
print(f"Fail: {percent_students_level_1:.2f}%")
print(f"Average: {average_grade:.2f}")
