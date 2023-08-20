budget = float(input())
price_kg_flour = float(input())

pack_eggs = price_kg_flour * 0.75
price_ltr_milk = price_kg_flour * 1.25
price_milk_per_loaf = price_ltr_milk / 4
price_per_loaf = pack_eggs + price_kg_flour + price_milk_per_loaf

left_budget = budget
count_coloured_eggs = 0
count_loafs = 0

while left_budget >= price_per_loaf:
    count_loafs += 1
    count_coloured_eggs += 3
    if count_loafs % 3 == 0:
        count_coloured_eggs -= count_loafs - 2
    left_budget -= price_per_loaf

print(f"You made {count_loafs} loaves of Easter bread! Now you have {count_coloured_eggs} eggs and {left_budget:.2f}BGN left.")