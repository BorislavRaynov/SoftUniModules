count_jorey = int(input())
presentation = input()

sum_grades = 0
total_ave = 0
count_presentation = 0

while presentation != "Finish":
    count_presentation += 1
    for i in range(1, count_jorey + 1):
        grade = float(input())
        sum_grades += grade
        total_ave += grade
    average = sum_grades / count_jorey
    print(f"{presentation} - {average:.2f}.")
    sum_grades = 0
    presentation = input()

total_average = total_ave / count_presentation / count_jorey
print(f"Student's final assessment is {total_average:.2f}.")
