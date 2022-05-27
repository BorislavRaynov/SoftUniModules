wide_cake = int(input())
length_cake = int(input())

cake_pieces = wide_cake * length_cake
pieces_taken = 0

while pieces_taken <= cake_pieces:
    current_pieces = input()
    if current_pieces == "STOP":
        break
    else:
        pieces_taken += int(current_pieces)

diff = abs(pieces_taken - cake_pieces)

if pieces_taken > cake_pieces:
    print(f"No more cake left! You need {diff} pieces more.")
else:
    print(f"{diff} pieces are left.")
