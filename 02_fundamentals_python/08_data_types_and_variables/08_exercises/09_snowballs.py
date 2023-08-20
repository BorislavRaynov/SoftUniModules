number_snowballs = int(input())
value = 0
snowball_weight = 0
snowball_time = 0
snowball_quality = 0

for ball in range(number_snowballs):
    weight = int(input())
    time_to_target = int(input())
    quality = int(input())
    current_value = int((weight / time_to_target) ** quality)
    if current_value > value:
        value = current_value
        snowball_weight = weight
        snowball_time = time_to_target
        snowball_quality = quality
print(f"{snowball_weight} : {snowball_time} = {value} ({snowball_quality})")
