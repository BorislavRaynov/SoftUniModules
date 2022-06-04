exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

exam_minutes = exam_hour * 60 + exam_min
arrival_minutes = arrival_hour * 60 + arrival_min
arrival_time = ""
diff = abs(arrival_minutes - exam_minutes)

if arrival_minutes > exam_minutes:
    arrival_time = "Late"
    if diff < 60:
        print(arrival_time)
        print(f"{diff} minutes after the start")
    elif diff >= 60:
        late_hours = diff // 60
        late_minutes = diff % 60
        if late_minutes <= 9:
            print(arrival_time)
            print(f"{late_hours}:0{late_minutes} hours after the start")
        else:
            print(arrival_time)
            print(f"{late_hours}:{late_minutes} hours after the start")
elif 0 <= diff <= 30:
    arrival_time = "On time"
    if diff == 0:
        print(arrival_time)
    elif diff <= 30:
        print(arrival_time)
        print(f"{diff} minutes before the start")
elif diff > 30:
    arrival_time = "Early"
    if diff >= 60:
        early_hours = diff // 60
        early_minutes = diff % 60
        if early_minutes <= 9:
            print(arrival_time)
            print(f"{early_hours}:0{early_minutes} hours before the start")
        else:
            print(arrival_time)
            print(f"{early_hours}:{early_minutes} hours before the start")
    elif diff < 60:
        print(arrival_time)
        print(f"{diff} minutes before the start")
