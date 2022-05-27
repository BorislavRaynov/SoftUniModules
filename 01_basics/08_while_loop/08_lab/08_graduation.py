student_name = input()
current_class = 1
count_under = 0
sum_grade = 0
while current_class <= 12:
    grade = float(input())
    if grade < 4.00:
        count_under += 1
        if count_under == 2:
            break
        continue
    elif grade >= 4.00:
        current_class += 1
    sum_grade += grade
if count_under == 2:
    print(f"{student_name} has been excluded at {current_class} grade")
else:
    average_grade = sum_grade / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
