number_rooms = int(input())

total_free_chairs = 0
chairs_left = True

for room in range(1, number_rooms + 1):
    information = input().split()
    current_number_visitors = int(information[1])
    current_chairs = len(information[0])
    current_free_chairs = current_chairs - current_number_visitors
    if current_chairs < current_number_visitors:
        chairs_left = False
        print(f"{abs(current_free_chairs)} more chairs needed in room {room}")
    else:
        total_free_chairs += current_free_chairs
        continue

if chairs_left:
    print(f"Game On, {total_free_chairs} free chairs left")
