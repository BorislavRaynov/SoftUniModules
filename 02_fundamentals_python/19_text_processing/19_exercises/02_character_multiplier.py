str1, str2 = input().split()
total_sum = 0
diff = abs(len(str1) - len(str2))
if len(str1) > len(str2):
    for character in range(len(str2)):
        total_sum += ord(str1[character]) * ord(str2[character])
    for character in range(len(str1) - diff, len(str1)):
        total_sum += ord(str1[character])
elif len(str1) < len(str2):
    for character in range(len(str1)):
        total_sum += ord(str1[character]) * ord(str2[character])
    for character in range(len(str2) - diff, len(str2)):
        total_sum += ord(str2[character])
else:
    for character in range(len(str1)):
        total_sum += ord(str1[character]) * ord(str2[character])

print(total_sum)
