goal_money = int(input())
item_price = input()

card_payment = 0
sum_card_payment = 0
cash_payment = 0
sum_cash_payment = 0
total_payments = 0
sum_total_payment = 0

while item_price != "End":

    cash_price = int(item_price)
    card_price = int(input())

    if cash_price > 100:
        print("Error in transaction!")
    else:
        cash_payment += 1
        sum_cash_payment += cash_price
        print("Product sold!")
    if card_price < 10:
        print("Error in transaction!")
    else:
        card_payment += 1
        sum_card_payment += card_price
        print("Product sold!")

    total_payments = sum_cash_payment + sum_card_payment

    if total_payments >= goal_money:
        print(f"Average CS: {sum_cash_payment / cash_payment:.2f}")
        print(f"Average CC: {sum_card_payment / card_payment:.2f}")
        break
    item_price = input()

if item_price == "End" or goal_money > total_payments:
    print("Failed to collect required money for charity.")
