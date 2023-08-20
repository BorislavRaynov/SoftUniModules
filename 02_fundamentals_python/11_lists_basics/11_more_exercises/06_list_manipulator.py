list_of_numbers = list(map(int, input().split()))
command = input()

while command != "end":
    command = command.split()
    current_command = command[0]
    if current_command == "exchange":
        index = int(command[1])
        if 0 <= index <= len(list_of_numbers) - 1:
            first_substring = list_of_numbers[:index + 1:]
            second_substring = list_of_numbers[index + 1::]
            list_of_numbers = second_substring + first_substring
        else:
            print("Invalid index")

    elif current_command == "max" or current_command == "min":
        if current_command == "max":
            if command[1] == "even":
                even_lst = [num for num in list_of_numbers if num % 2 == 0]
                if not even_lst:
                    print("No matches")
                    command = input()
                    continue

                max_even = max(even_lst)
                if even_lst.count(max_even) > 1:
                    for num in range(len(list_of_numbers) - 1, -1, -1):
                        if list_of_numbers[num] == max_even:
                            index_max_even = num
                            print(index_max_even)
                else:
                    index_max_even = list_of_numbers.index(max_even)
                    print(index_max_even)

            elif command[1] == "odd":
                odd_lst = [num for num in list_of_numbers if num % 2 != 0]
                if not odd_lst:
                    print("No matches")
                    command = input()
                    continue

                max_odd = max(odd_lst)
                if odd_lst.count(max_odd) > 1:
                    for num in range(len(list_of_numbers) - 1, -1, -1):
                        if list_of_numbers[num] == max_odd:
                            index_max_odd = num
                            print(index_max_odd)
                else:
                    index_max_odd = list_of_numbers.index(max_odd)
                    print(index_max_odd)

        elif current_command == "min":
            if command[1] == "even":
                even_lst = [num for num in list_of_numbers if num % 2 == 0]
                if not even_lst:
                    print("No matches")
                    command = input()
                    continue

                min_even = min(even_lst)
                if even_lst.count(min_even) > 1:
                    for num in range(len(list_of_numbers) - 1, -1, -1):
                        if list_of_numbers[num] == min_even:
                            index_min_even = num
                            print(index_min_even)
                else:
                    index_min_even = list_of_numbers.index(min_even)
                    print(index_min_even)

            elif command[1] == "odd":
                odd_lst = [num for num in list_of_numbers if num % 2 != 0]
                if not odd_lst:
                    print("No matches")
                    command = input()
                    continue

                min_odd = min(odd_lst)
                if odd_lst.count(min_odd) > 1:
                    for num in range(len(list_of_numbers) - 1, -1, -1):
                        if list_of_numbers[num] == min_odd:
                            index_min_odd = num
                            print(index_min_odd)
                else:
                    index_min_odd = list_of_numbers.index(min_odd)
                    print(index_min_odd)

    elif current_command == "first":
        count_numbers = int(command[1])
        if count_numbers > len(list_of_numbers):
            print("Invalid count")
            command = input()
            continue
        if command[2] == "even":
            counter_even = 0
            nums_to_be_printed = []
            for num in list_of_numbers:
                if num % 2 == 0:
                    counter_even += 1
                    nums_to_be_printed.append(num)
                    if counter_even >= count_numbers:
                        break
            print(nums_to_be_printed)
        elif command[2] == "odd":
            counter_odd = 0
            nums_to_be_printed = []
            for num in list_of_numbers:
                if num % 2 != 0:
                    counter_odd += 1
                    nums_to_be_printed.append(num)
                    if counter_odd >= count_numbers:
                        break
            print(nums_to_be_printed)

    elif current_command == "last":
        count_numbers = int(command[1])
        if count_numbers > len(list_of_numbers):
            print("Invalid count")
            command = input()
            continue
        if command[2] == "even":
            counter_even = 0
            nums_to_be_printed = []
            for num in list_of_numbers[len(list_of_numbers)::-1]:
                if num % 2 == 0:
                    counter_even += 1
                    nums_to_be_printed.append(num)
                    if counter_even >= count_numbers:
                        break
            print(nums_to_be_printed)
        elif command[2] == "odd":
            counter_odd = 0
            nums_to_be_printed = []
            for num in list_of_numbers[len(list_of_numbers)::-1]:
                if num % 2 != 0:
                    counter_odd += 1
                    nums_to_be_printed.append(num)
                    if counter_odd >= count_numbers:
                        break
            print(nums_to_be_printed)

    command = input()

print(list_of_numbers)
