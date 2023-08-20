from os import linesep
from collections import deque

with open('text.txt', 'r') as current_text:
    symbols_to_replace = ["-", ",", ".", "!", "?"]
    counter_line = 0

    for line in current_text:

        if counter_line % 2 == 0:
            output_line = deque()
            split_line = line.split()

            for word in split_line:
                current_word = ""

                for char in word:
                    if char == linesep:
                        continue
                    if char in symbols_to_replace:
                        char = "@"
                    current_word += char

                output_line.appendleft(current_word)

            print(" ".join(output_line))

        counter_line += 1
