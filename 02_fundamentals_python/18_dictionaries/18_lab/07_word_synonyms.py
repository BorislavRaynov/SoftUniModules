num = int(input())
synonyms_dictionary = dict()

for word in range(num):
    current_word = input()
    current_synonym = input()
    if current_word not in synonyms_dictionary:
        synonyms_dictionary[current_word] = []
    synonyms_dictionary[current_word].append(current_synonym)

for word in synonyms_dictionary:
    print(f"{word} - {', '.join(synonyms_dictionary[word])}")
