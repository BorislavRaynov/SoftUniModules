number_electrons = int(input())

current_shell = 1
total_shells = []

while sum(total_shells) < number_electrons:
    total_shells.append(2*current_shell**2)
    current_shell += 1

last_shell = number_electrons - (sum(total_shells) - total_shells[-1])
total_shells.pop(-1)
total_shells.append(last_shell)

print(total_shells)
