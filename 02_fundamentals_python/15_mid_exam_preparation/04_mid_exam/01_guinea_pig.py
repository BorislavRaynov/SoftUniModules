food_per_month = float(input())
hay_per_month = float(input())
cover_per_month = float(input())
weight_pig = float(input()) * 1000

enough_food = True
enough_hay = True
enough_cover = True

excess_food = food_per_month * 1000
excess_hay = hay_per_month * 1000
excess_cover = cover_per_month * 1000

for day in range(1, 31):
    excess_food -= 300
    if excess_food <= 0:
        enough_food = False
        break
    if day % 2 == 0:
        excess_hay -= excess_food * 0.05
        if excess_hay <= 0:
            enough_hay = False
    if day % 3 == 0:
        excess_cover -= weight_pig / 3
        if excess_cover <= 0:
            enough_cover = False
            break

if enough_food and enough_hay and enough_cover:
    print(f"Everything is fine! Puppy is happy! Food:\
 {excess_food / 1000:.2f}, Hay: {(excess_hay / 1000):.2f}, Cover: {excess_cover / 1000:.2f}.")
else:
    print("Merry must go to the pet store!")
