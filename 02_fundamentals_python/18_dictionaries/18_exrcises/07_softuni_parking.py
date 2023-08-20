number_of_commands = int(input())
parking_lot = {}
for car in range(number_of_commands):
    command = input().split()
    username = command[1]
    if command[0] == "register":
        license_plate = command[2]
        if username not in parking_lot:
            parking_lot[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_lot[username]}")
    elif command[0] == "unregister":
        if username not in parking_lot:
            print(f"ERROR: user {username} not found")
        else:
            parking_lot.pop(username)
            print(f"{username} unregistered successfully")

for username, license_plate in parking_lot.items():
    print(f"{username} => {license_plate}")
