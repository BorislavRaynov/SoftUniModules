lst_of_cards = input().split(", ")
number = int(input())

for command in range(1, number + 1):
    command_split = input().split(", ")
    current_command = command_split[0]
    if current_command == "Add":
        card_name = command_split[1]
        if card_name in lst_of_cards:
            print("Card is already in the deck")
            continue
        else:
            lst_of_cards.append(card_name)
            print("Card successfully added")
    elif current_command == "Remove":
        current_card_name = command_split[1]
        if current_card_name in lst_of_cards:
            index_card = lst_of_cards.index(current_card_name)
            lst_of_cards.pop(index_card)
            print("Card successfully removed")
        else:
            print("Card not found")
    elif current_command == "Remove At":
        index = int(command_split[1])
        if 0 <= index <= len(lst_of_cards) - 1:
            lst_of_cards.pop(index)
            print("Card successfully removed")
        else:
            print("Index out of range")
    elif current_command == "Insert":
        current_index = int(command_split[1])
        new_card_name = command_split[2]
        if 0 <= current_index <= len(lst_of_cards) - 1:
            if new_card_name in lst_of_cards:
                print("Card is already added")
                continue
            else:
                lst_of_cards.insert(current_index, new_card_name)
                print("Card successfully added")
        else:
            print("Index out of range")

print(", ".join(lst_of_cards))
