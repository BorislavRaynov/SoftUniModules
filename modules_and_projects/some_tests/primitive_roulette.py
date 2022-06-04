import random
print("Добър ден. Добре дошли в Primitive Bet Casino.")
print()
print("В момента сте седнали на маса за игра на нашата примитивна рулетка.")
print()
times_bet = int(input("Моля въведете колко пъти искате да играете?(1-10): "))
print()
print("Ако не желаете да залагате на някоя от следващите позиции пропуснете като натисните ENTER.")
print()
amount_bet = int(input("Моля въведете стойност на залог за всяка желана позиция:(1-100) "))
print()
print("Ок да започваме и успех :)")
print()

all_numbers = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
fst_dozen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
snd_dozen = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
trd_dozen = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
trd_line = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
snd_line = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
fst_line = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
fst_half = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
snd_half = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

current_colour = ""
current_type_number = ""
current_dozen = ""
current_line = ""
current_half = ""
profit = 0
loses = 0
total_sum = profit - loses

for bet in range(1, times_bet + 1):

    number = input("Желаете ли да заложите на число:(1-36) ")
    print()
    colour = input("Желаете ли да заложите на цвят?:(red-black) ")
    print()
    even_or_not = input("Желаете ли да заложите дали е четно или нечетно?:(even-odd) ")
    print()
    line = input("Желате ли да заложите на линия от числа?:(1st/2nd/3rd) ")
    print()
    dozen = input("Желаете ли да заложите на дузина от числа?:(1st/2nd/3rd) ")
    print()
    half = input("Желаете ли да заложите на половина от числа?:(1st/2nd) ")

    current_number = random.choice(all_numbers)

    if number != "":
        if current_number == int(number):
            profit += 36 * amount_bet
        else:
            loses += amount_bet

    if colour != "":
        if current_number in red:
            current_colour = "red"
        elif current_number in black:
            current_colour = "black"
        if colour == current_colour:
            profit += 2 * amount_bet
        elif colour != current_colour:
            loses += amount_bet

    if even_or_not != "":
        if current_number in even:
            current_type_number = "even"
        elif current_number in odd:
            current_type_number = "odd"
        if even_or_not == current_type_number:
            profit += 2 * amount_bet
        elif even_or_not != current_type_number:
            loses += amount_bet

    if line != "":
        if current_number in fst_line:
            current_line = "1st"
        elif current_number in snd_line:
            current_line = "2nd"
        elif current_number in trd_line:
            current_line = "3rd"
        if line == current_line:
            profit += 2 * amount_bet
        elif line != current_line:
            loses += amount_bet

    if dozen != "":
        if current_number in fst_dozen:
            current_dozen = "1st"
        elif current_number in snd_dozen:
            current_dozen = "2nd"
        elif current_number in trd_dozen:
            current_dozen = "3rd"
        if dozen == current_dozen:
            profit += 2 * amount_bet
        elif dozen != current_dozen:
            loses += amount_bet

    if half != "":
        if current_number in fst_half:
            current_half = "1st"
        elif current_number in snd_half:
            current_half = "2nd"
        if half == current_half:
            profit += 2 * amount_bet
        elif half != current_half:
            loses += amount_bet

    print(f"Изтегленото число е: {current_number}")

if total_sum > 0:
    print(f"Поздравления !!! Днес спечелихте {total_sum}лв. Движдане.")
elif total_sum == 0:
    print("Днес нито спечелихте, но по-важното е ,че не изгубихте :). До нови срещи.")
else:
    print(f"Съжаляваме, но днес изгубихте {abs(total_sum)}лв. Доскоро.")
