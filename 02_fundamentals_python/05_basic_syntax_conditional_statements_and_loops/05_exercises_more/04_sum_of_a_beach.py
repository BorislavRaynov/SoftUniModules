string = input()

count_words = 0

count_words += string.lower().count("sand")
count_words += string.lower().count("water")
count_words += string.lower().count("fish")
count_words += string.lower().count("sun")

print(count_words)
