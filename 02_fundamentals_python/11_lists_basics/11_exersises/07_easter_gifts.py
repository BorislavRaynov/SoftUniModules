list_of_gifts = input().split()
current_list = list_of_gifts

command = input()

gift = ""
index = ""
split_command = []

while command != "No Money":
    if "OutOfStock" in command:
        split_command = command.split()
        gift = split_command[1]
        while gift in current_list:
            current_index = current_list.index(gift)
            current_list[current_index] = "None"
    elif "Required" in command:
        split_command = command.split()
        gift = split_command[1]
        index = split_command[2]
        if 0 <= int(index) <= len(current_list):
            current_list[int(index)] = gift
    elif "JustInCase" in command:
        split_command = command.split()
        gift = split_command[1]
        current_list[-1] = gift
    command = input()


while "None" in current_list:
    current_list.remove("None")
print(" ".join(current_list))
