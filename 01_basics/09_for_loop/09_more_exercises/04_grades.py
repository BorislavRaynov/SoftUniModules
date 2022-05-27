count_students = int(input())

count_f = 0
count_d = 0
count_c = 0
count_b = 0
total_grade = 0
for i in range(1, count_students + 1):
    grade = float(input())
    if 2.00 <= grade <= 2.99:
        count_f += 1
        total_grade += grade
    elif grade <= 3.99:
        count_d += 1
        total_grade += grade
    elif grade <= 4.99:
        count_c += 1
        total_grade += grade
    elif grade >= 5.00:
        count_b += 1
        total_grade += grade

f_percent = (count_f / count_students) * 100
d_percent = (count_d / count_students) * 100
c_percent = (count_c / count_students) * 100
b_percent = (count_b / count_students) * 100
average_grade = total_grade / count_students

print(f"Top students: {b_percent:.2f}%")
print(f"Between 4.00 and 4.99: {c_percent:.2f}%")
print(f"Between 3.00 and 3.99: {d_percent:.2f}%")
print(f"Fail: {f_percent:.2f}%")
print(f"Average: {average_grade:.2f}")