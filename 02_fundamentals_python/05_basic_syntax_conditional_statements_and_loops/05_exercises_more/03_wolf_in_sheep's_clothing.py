herd_list = input().split(", ")
current_number_sheep = 0

if herd_list.pop() == "wolf":
    print("Please go away and stop eating my sheep")
elif "wolf" in herd_list:
    herd_list.reverse()
    for element in herd_list:
        current_number_sheep += 1
        if element == "wolf":
            break
    # for number, sheep in enumerate(herd_list):
    #     current_number_sheep += 1
    #     if sheep == "wolf":
    #         break
    print(f"Oi! Sheep number {current_number_sheep}! You are about to be eaten by a wolf!")
