command = input()
notes = []
while command != "End":
    tokens = command.split("-")
    task = tokens[1]
    priority = int(tokens[0])
    notes.append((priority, task))
    command = input()
sorted_notes = [i[1] for i in sorted(notes)]
print(sorted_notes)
