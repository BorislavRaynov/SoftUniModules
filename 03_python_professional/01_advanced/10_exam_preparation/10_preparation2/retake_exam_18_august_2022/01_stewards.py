from collections import deque

seats = input().split(', ')
first_seq = deque(map(int, input().split(', ')))
second_seq = deque(map(int, input().split(', ')))


rotations = 0
found_seats = []

while rotations < 10 and len(found_seats) < 3:
    rotations += 1
    first_num = first_seq.popleft()
    sec_num = second_seq.pop()
    current_char = chr(first_num + sec_num)
    for seat in seats:
        seat_symbol = seat[-1]
        if seat_symbol == current_char:
            found_seats.append(seat)
            seats.remove(seat)
            break
    else:
        first_seq.append(first_num)
        second_seq.appendleft(sec_num)

print(f"Seat matches: {', '.join(found_seats)}")
print(f"Rotations count: {rotations}")
