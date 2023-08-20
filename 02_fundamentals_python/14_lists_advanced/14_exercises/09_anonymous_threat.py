given_string = input().split()
command = input()


divided_current_string = []

while command != "3:1":
    command = command.split()
    if command[0] == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        current_string = ""
        if end_index > len(given_string) - 1:
            end_index = len(given_string) - 1
        elif start_index < 0:
            start_index = 0
        for i in range(start_index, end_index + 1):
            current_string += given_string[i]
            given_string[i] = "0"
        given_string = [word for word in given_string if word != "0"]
        given_string.insert(start_index, current_string)

    elif command[0] == "divide":
        index = int(command[1])
        partition = int(command[2])
        final_to_be_added = []
        word_to_be_divided = given_string[index]
        substring_len = len(word_to_be_divided) // partition

        if len(word_to_be_divided) % partition == 0:
            for i in range(len(word_to_be_divided)):
                current_string = ""
                for character in range(partition):
                    current_string += word_to_be_divided
        elif len(word_to_be_divided) % partition != 0:
            start_loop = 0
            end_loop = decimal
            while end_loop < len(word_to_be_divided):
                current_word = ""
                for character in range(start_loop, end_loop):
                    current_word += word_to_be_divided[character]
                divided_current_string.append(current_word)
                start_loop += decimal
                end_loop += decimal
            given_string.remove(word_to_be_divided)
            divided_current_string[-1] += word_to_be_divided[-1]

    command = input()


final_string = given_string + divided_current_string
print(" ".join(final_string))
