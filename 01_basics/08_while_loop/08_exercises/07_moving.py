wide_app = int(input())
length_app = int(input())
height_app = int(input())

volume_app = wide_app * length_app * height_app
volume_box = 1
volume_needed = 0

while volume_needed <= volume_app:
    count_box = input()
    if count_box == "Done":
        break
    else:
        volume_needed += int(count_box)

diff = abs(volume_needed - volume_app)
if volume_needed > volume_app:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")
