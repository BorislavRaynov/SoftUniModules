box_of_clothes = list(map(int, input().split()))
rack_capacity = int(input())
current_value = 0
rack_count = 1

for clothe in range(len(box_of_clothes)):
    clothe_value = box_of_clothes[-1]
    box_of_clothes.pop()
    current_value += clothe_value
    if current_value == rack_capacity:
        if len(box_of_clothes) > 0:
            rack_count += 1
            current_value = 0
    elif current_value > rack_capacity:
        rack_count += 1
        current_value = 0
        current_value += clothe_value

print(rack_count)
