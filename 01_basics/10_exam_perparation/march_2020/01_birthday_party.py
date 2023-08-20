rent = float(input())

price_cake = rent * 0.20
price_drinks = price_cake * 0.55
animation_drinks = rent / 3

budget_needed = price_cake + price_drinks + animation_drinks + rent

print(f"{budget_needed}")
