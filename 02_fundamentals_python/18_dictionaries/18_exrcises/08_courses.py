command = input()
courses_students = {}

while command != "end":
    current_command = command.split(" : ")
    course_name = current_command[0]
    student_name = current_command[1]
    if course_name not in courses_students:
        courses_students[course_name] = []
    courses_students[course_name].append(student_name)

    command = input()
for course, name in courses_students.items():
    print(f"{course}: {len(courses_students[course])}")
    for value in courses_students[course]:
        print(f"-- {value}")
