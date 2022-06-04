budget = int(input())
price = input()

current_budget = budget
while price != "End":
    price = int(price)
    current_budget -= price
    if current_budget < 0:
        print("You went in overdraft!")
        break
    price = input()
else:
    print("You bought everything needed.")
