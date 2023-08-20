def palindrome(string, idx):
    if idx == len(string) // 2:
        return f"{string} is a palindrome"

    first, last = string[idx], string[-1 - idx]
    if first != last:
        return f"{string} is not a palindrome"

    return palindrome(string, idx + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
