from math import ceil
name = input()
episode_sec = int(input())
break_time = int(input())

lunch_time = break_time / 8
relax_time = break_time / 4
left_time = break_time - lunch_time - relax_time
diff = abs(episode_sec - left_time)

if episode_sec <= left_time:
    print(f'You have enough time to watch {name} and left with {ceil(diff)} minutes free time.')
else:
    print(f"You don't have enough time to watch {name}, you need {ceil(diff)} more minutes.")