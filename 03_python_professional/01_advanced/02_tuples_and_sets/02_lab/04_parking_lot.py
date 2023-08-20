count_commands = int(input())
parking_lot = set()
for car in range(count_commands):
    direction, plate = input().split(", ")
    if direction == "IN":
        parking_lot.add(plate)
    else:
        parking_lot.remove(plate)

if len(parking_lot) == 0:
    print("Parking Lot is Empty")
else:
    print("\n".join(parking_lot))
