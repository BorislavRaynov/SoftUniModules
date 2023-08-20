from string import punctuation

with open('./text.txt') as input_file, open('./output.txt', 'a') as output_file:
    current_count_line = 1

    for line in input_file:
        current_count_letters = 0
        current_count_marks = 0
        current_line = line.split()

        for word in current_line:
            for char in word:
                if char.isalpha():
                    current_count_letters += 1
                elif char in punctuation:
                    current_count_marks += 1

        output_file.write(f"Line {current_count_line}: \
{line.strip()} ({current_count_letters})({current_count_marks})\n")

        current_count_line += 1
