import re

text = input()

pattern = r'\@([A-Za-z]{3,})\@\@([A-Za-z]{3,})\@|\#([A-Za-z]{3,})\#\#([A-Za-z]{3,})\#'
all_pairs = []
all_words = []
mirror_words = []

result = re.finditer(pattern, text)

for match in result:
    all_pairs.append(match.group())
    for word in match.groups():
        if word:
            all_words.append(word)

for i in range(0, len(all_words), 2):
    first_word = all_words[i]
    second_word = all_words[i + 1]
    if first_word == second_word[::-1]:
        pair = f"{first_word} <=> {second_word}"
        mirror_words.append(pair)

if len(all_pairs) == 0:
    print("No word pairs found!")
else:
    print(f"{len(all_pairs)} word pairs found!")
if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirror_words))
