array_values = list(map(int, input().split()))
command = input()

while command != "end":
    split_command = command.split()
    current_command = split_command[0]

    if current_command == "swap":
        first_index = int(split_command[1])
        second_index = int(split_command[2])
        array_values[first_index], array_values[second_index] = array_values[second_index], array_values[first_index]

    elif current_command == "multiply":
        first_index = int(split_command[1])
        second_index = int(split_command[2])
        result = array_values[first_index] * array_values[second_index]
        array_values.pop(first_index)
        array_values.insert(first_index, result)

    elif current_command == "decrease":
        for num in range(len(array_values)):
            array_values[num] -= 1

    command = input()

print(", ".join(list(map(str, array_values))))
