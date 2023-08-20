text = input()
vowels_lst = ["a", "o", "u", "e", "i", "A", "O", "U", "E", "I"]

new_text = "".join([ch for ch in text if ch not in vowels_lst])
print(new_text)
