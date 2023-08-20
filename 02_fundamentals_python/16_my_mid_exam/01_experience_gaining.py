needed_experience = float(input())
count_battles = int(input())

current_battles = 0
experience_left = needed_experience
experience_is_collected = False

for battle in range(1, count_battles + 1):
    earned_experience = float(input())
    if battle % 15 == 0:
        earned_experience *= 1.05
        if battle % 5 == 0:
            earned_experience *= 0.9
        if battle % 3 == 0:
            earned_experience *= 1.15
    elif battle % 5 == 0:
        earned_experience *= 0.9
        if battle % 3 == 0:
            earned_experience *= 1.15
    elif battle % 3 == 0:
        earned_experience *= 1.15
    # elif battle % 5 == 0:
    #     earned_experience *= 0.9
    # elif battle % 15 == 0:
    #     earned_experience *= 1.05
    experience_left -= earned_experience
    current_battles += 1
    if experience_left <= 0:
        experience_is_collected = True
        break

if experience_is_collected:
    print(f"Player successfully collected his needed experience for {current_battles} battles.")
else:
    print(f"Player was not able to collect the needed experience, {experience_left:.2f} more needed.")
