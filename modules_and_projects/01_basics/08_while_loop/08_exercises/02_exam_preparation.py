count_not_good_grades = int(input())

total_grade = 0
count_total_tasks = 0
last_task = ""
count_failed_grades = 0
has_failed = False
task_name = input()

while task_name != "Enough":
    grade = int(input())
    if grade <= 4:
        count_failed_grades += 1

    last_task = task_name

    count_total_tasks += 1
    total_grade += grade
    if count_failed_grades == count_not_good_grades:
        has_failed = True
        break
    task_name = input()

if has_failed:
    print(f"You need a break, {count_failed_grades} poor grades.")
else:
    average_grade = total_grade / count_total_tasks
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {count_total_tasks}")
    print(f"Last problem: {last_task}")
