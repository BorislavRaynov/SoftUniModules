favorite_book = input()
book = input()
count_book = 0
while book != "No More Books":
    if book == favorite_book:
        break
    else:
        count_book += 1
    book = input()
if book == favorite_book:
    print(f"You checked {count_book} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {count_book} books.")
