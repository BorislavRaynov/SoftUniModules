lst_all = input().split()
searched_palindrome = input()
palindrome_lst = [element for element in lst_all if element[::1] == element[::-1]]

print(palindrome_lst)
palindrome_count = palindrome_lst.count(searched_palindrome)
print(f"Found palindrome {palindrome_count} times")
