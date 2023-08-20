some_elements = input().split()
nums = input()

current_move = 0
all_elements_are_found = False

while nums != "end":
    current_nums = nums.split()
    first_index = int(current_nums[0])
    second_index = int(current_nums[1])

    if (0 <= first_index <= len(some_elements) - 1 and 0 <= second_index <= len(some_elements) - 1)\
            and first_index != second_index:
        current_move += 1
        if some_elements[first_index] == some_elements[second_index]:
            found_element = some_elements[first_index]
            some_elements = [num for num in some_elements if num != some_elements[first_index]]
            print(f"Congrats! You have found matching elements - {found_element}!")
        else:
            print("Try again!")
    else:
        current_move += 1
        element_to_be_added = f"{-current_move}a"
        the_middle = len(some_elements) // 2
        some_elements.insert(the_middle, element_to_be_added)
        some_elements.insert(the_middle, element_to_be_added)
        print("Invalid input! Adding additional elements to the board")

    if len(some_elements) == 0:
        all_elements_are_found = True
        break

    nums = input()

if all_elements_are_found:
    print(f"You have won in {current_move} turns!")
else:
    print("Sorry you lose :(")
    print(" ".join(some_elements))

