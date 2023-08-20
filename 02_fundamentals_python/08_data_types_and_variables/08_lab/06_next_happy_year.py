given_year = int(input())

happy_new_year_is_found = False


while not happy_new_year_is_found:
    given_year += 1
    special_year = set()
    for i in range(len(str(given_year))):
        special_year.add(str(given_year)[i])

    happy_new_year_is_found = len(special_year) == len(str(given_year))

print(given_year)
