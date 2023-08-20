deposit = input()
sum_of_deposit = 0

while deposit != "NoMoreMoney":
    current_deposit = float(deposit)
    if current_deposit < 0:
        print(f"Invalid operation!")
        break
    print(f"Increase: {current_deposit:.2f}")
    sum_of_deposit += current_deposit
    deposit = input()
print(f"Total: {sum_of_deposit:.2f}")