command = input()
users = {}
submissions = {}


while command != "exam finished":
    current_command = command.split("-")
    username = current_command[0]
    if "banned" in current_command:
        for key, value in users.items():
            if username in value:
                users[key].pop(username)

    else:
        language = current_command[1]
        points = int(current_command[2])
        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1
        if language not in users:
            users[language] = {username: points}
        if username not in users[language]:
            users[language][username] = points
        if users[language][username] < points:
            users[language][username] = points

    command = input()

print("Results:")
for key, value in users.items():
    for nested_key, nested_value in value.items():
        print(f"{nested_key} | {nested_value}")
print("Submissions:")
for key, value in submissions.items():
    print(f"{key} - {value}")

