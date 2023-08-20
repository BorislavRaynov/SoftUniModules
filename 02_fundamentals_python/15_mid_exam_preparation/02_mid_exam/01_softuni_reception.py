first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
count_students = int(input())

needed_hours = 0
breaks = 0
total_students_hour = first_employee + second_employee + third_employee

while count_students > 0:
    count_students -= total_students_hour
    needed_hours += 1
    if needed_hours % 3 == 0 and 0 < count_students:
        breaks += 1

print(f"Time needed: {needed_hours + breaks}h.")

