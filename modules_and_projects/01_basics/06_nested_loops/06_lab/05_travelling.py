destination = input()

total_saved = 0

while destination != "End":
    needed_money = float(input())
    while total_saved < needed_money:
        money_saved = float(input())
        total_saved += money_saved
    if total_saved >= needed_money:
        print(f"Going to {destination}!")
    destination = input()
    total_saved = 0
