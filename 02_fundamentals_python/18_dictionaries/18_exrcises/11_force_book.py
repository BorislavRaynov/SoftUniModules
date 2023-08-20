input_line = input()
users = {}

while input_line != "Lumpawaroo":
    if "|" in input_line:
        force_side, force_user = input_line.split(" | ")
        user_exist = False
        for value in users.values():
            if force_user in value:
                user_exist = True
                break
        if not user_exist:
            if force_side not in users:
                users[force_side] = [force_user]
            else:
                users[force_side].append(force_user)

    elif "->" in input_line:
        force_user, force_side = input_line.split(" -> ")
        for key, value in users.items():
            if force_user in value:
                users[key].pop(value.index(force_user))
                break
        if force_side not in users:
            users[force_side] = [force_user]
        else:
            users[force_side] += [force_user]
        print(f"{force_user} joins the {force_side} side!")

    input_line = input()

for force_side in users:
    if len(users[force_side]) > 0:
        print(f"Side: {force_side}, Members: {len(users[force_side])}")
        [print(f"! {user}") for user in users[force_side]]
    