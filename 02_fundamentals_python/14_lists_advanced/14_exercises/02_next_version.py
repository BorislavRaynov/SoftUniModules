current_version = list(map(int, input().split(".")))

next_version = [current_version[0], current_version[1], current_version[2] + 1]
for i in range(len(next_version) - 1, - 1, - 1):
    if next_version[i] > 9:
        next_version[i] = 0
        next_version[i - 1] += 1

new_version = list(map(str, next_version))
print(".".join(new_version))
