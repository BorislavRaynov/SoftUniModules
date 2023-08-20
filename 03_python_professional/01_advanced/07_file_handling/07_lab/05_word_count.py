import re
words_dict = {}
with open('./words.txt') as words_file:
    all_words = words_file.read().split()
    for word in all_words:
        words_dict[word] = 0

with open('./input.txt') as input_file:
    for line in input_file:
        all_line_words = re.findall("[a-zA-Z\']+", line)
        for word in all_line_words:
            word_lower = word.lower()
            if word_lower in words_dict:
                words_dict[word_lower] += 1

with open('./output.txt', 'w') as output_file:
    sorted_dict = sorted(words_dict.items(), key=lambda x: -x[1])
    for key, value in sorted_dict:
        output_file.write(f"{key} - {value}\n")
