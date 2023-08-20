def num_palindrome(a):
    for element in a:
        current_num = element[::1]
        new_num = element[::-1]
        if current_num == new_num:
            print(True)
        else:
            print(False)


list_of_numbers = input().split(", ")
num_palindrome(list_of_numbers)
