count_loses = int(input())
helmet_price= float(input())
sword_price= float(input())
shield_price= float(input())
armor_price= float(input())
total_price = 0

total_price += count_loses // 2 * helmet_price
total_price += count_loses // 3 * sword_price
total_price += count_loses // 6 * shield_price
total_price += count_loses // 12 * armor_price

print(f"Gladiator expenses: {total_price:.2f} aureus")
