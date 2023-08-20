bottles_detergent = int(input())

mltrs_detergent = bottles_detergent * 750
total_detergent = mltrs_detergent
load = 0
count_dishes = 0
count_pods = 0
detergent_has_finished = False

command = input()

while command != "End":
    command = int(command)
    load += 1

    if load % 3 == 0:
        count_pods += command
        total_detergent -= command * 15
    else:
        count_dishes += command
        total_detergent -= command * 5
    if total_detergent < 0:
        detergent_has_finished = True
        break
    command = input()

if detergent_has_finished:
    print(f"Not enough detergent, {abs(total_detergent)} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{count_dishes} dishes and {count_pods} pots were washed.")
    print(f"Leftover detergent {total_detergent} ml.")
