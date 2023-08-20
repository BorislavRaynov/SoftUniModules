total_pumps = int(input())
fuel_in_tank = 0
searched_pump = 0

for pump in range(total_pumps):
    pump_info = list(map(int, input().split()))
    amount_of_petrol = pump_info[0]
    distance_to_next = pump_info[1]
    fuel_in_tank += amount_of_petrol
    if fuel_in_tank < distance_to_next:
        searched_pump = pump + 1
        fuel_in_tank = 0
    else:
        fuel_in_tank -= distance_to_next

print(searched_pump)
