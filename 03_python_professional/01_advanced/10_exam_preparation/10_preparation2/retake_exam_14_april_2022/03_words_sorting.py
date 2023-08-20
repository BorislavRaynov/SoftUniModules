def words_sorting(*args):
    sum_of_all_values = 0
    words = {}
    result = ''
    for el in args:
        current_word_value = 0
        for char in el:
            current_word_value += ord(char)
        sum_of_all_values += current_word_value
        if el not in words:
            words[el] = 0
        words[el] += current_word_value

    if sum_of_all_values % 2 == 0:
        for key, value in sorted(words.items(), key=lambda x: x[0]):
            result += f"{key} - {value}\n"
    else:
        for key, value in sorted(words.items(), key=lambda x: -x[1]):
            result += f"{key} - {value}\n"

    return result


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
