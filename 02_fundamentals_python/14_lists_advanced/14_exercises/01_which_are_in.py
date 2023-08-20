first_string = input().split(", ")
second_string = input().split(", ")

subs_string = []

for word in first_string:
    for second_word in second_string:
        if word in second_word and not word in subs_string:
            subs_string.append(word)

print(subs_string)
