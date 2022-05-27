count_tabs = int(input())
salary = float(input())

salary_left = salary
for i in range(1, count_tabs + 1):
    tab = input()
    if tab == "Facebook":
        salary_left -= 150
    elif tab == "Instagram":
        salary_left -= 100
    elif tab == "Reddit":
        salary_left -= 50
    if salary_left <= 0:
        break
if salary_left <= 0:
    print("You have lost your salary.")
else:
    print(f"{round(salary_left)}")