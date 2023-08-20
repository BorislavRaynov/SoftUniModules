initial_pieces = int(input())
pieces_dict = {}

for piece in range(initial_pieces):
    piece_name, composer, key = input().split("|")
    if key not in pieces_dict:
        pieces_dict[piece_name] = []
    pieces_dict[piece_name] += composer, key

command = input()

while command != "Stop":
    current_command = command.split("|")
    to_do = current_command[0]
    current_piece_name = current_command[1]
    if to_do == "Add":
        current_composer = current_command[2]
        current_key = current_command[3]
        if current_piece_name not in pieces_dict:
            pieces_dict[current_piece_name] = [current_composer, current_key]
            print(f"{current_piece_name} by {current_composer} in {current_key} added to the collection!")
        else:
            print(f"{current_piece_name} is already in the collection!")
    elif to_do == "Remove":
        if current_piece_name in pieces_dict:
            pieces_dict.pop(current_piece_name)
            print(f"Successfully removed {current_piece_name}!")
        else:
            print(f"Invalid operation! {current_piece_name} does not exist in the collection.")
    elif to_do == "ChangeKey":
        new_key = current_command[2]
        if current_piece_name in pieces_dict:
            pieces_dict[current_piece_name][1] = new_key
            print(f"Changed the key of {current_piece_name} to {new_key}!")
        else:
            print(f"Invalid operation! {current_piece_name} does not exist in the collection.")
    command = input()

for key, value in pieces_dict.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
