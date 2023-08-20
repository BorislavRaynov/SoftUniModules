chicken = int(input())
fish = int(input())
veg = int(input())

ch_menu = chicken * 10.35
fish_menu = fish * 12.40
veg_menu = veg * 8.15
delivery = 2.5
dessert = (ch_menu + fish_menu + veg_menu) * 0.2

final_price = ch_menu + fish_menu + veg_menu + dessert + delivery
print(final_price)
