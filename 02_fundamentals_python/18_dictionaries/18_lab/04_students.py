command = input()
students_info = {}

while ":" in command:
    info = command.split(":")
    name,  id, course = info[0], info[1], info[2]
    if course not in students_info:
        students_info[course] = {}
    students_info[course][id] = name
    command = input()

course = " ".join(command.split("_"))
for key, value in students_info.items():
    if key == course:
        for id, name in value.items():
            print(f"{name} - {id}")
