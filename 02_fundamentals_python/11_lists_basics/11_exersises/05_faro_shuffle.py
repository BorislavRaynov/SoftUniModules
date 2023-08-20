initial_deck = input().split()
shuffles = int(input())

for shuffle in range(shuffles):
    final_deck = []
    middle_of_deck = len(initial_deck) // 2
    first_half = initial_deck[:middle_of_deck:]
    second_half = initial_deck[middle_of_deck::]
    for card in range(len(first_half)):
        final_deck.append(first_half[card])
        final_deck.append(second_half[card])
    initial_deck = final_deck
print(initial_deck)
