count_day_offs = int(input())
tom_min_play = 30000

days_at_work = 365 - count_day_offs
min_when_dayoff = count_day_offs * 127
min_when_work = days_at_work * 63
total_play_mins = min_when_dayoff + min_when_work

h_play_time = abs(tom_min_play - total_play_mins) // 60
m_play_time = abs(tom_min_play - total_play_mins) % 60

if tom_min_play < total_play_mins:
    print("Tom will run away")
    print(f"{h_play_time} hours and {m_play_time} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{h_play_time} hours and {m_play_time} minutes less for play")