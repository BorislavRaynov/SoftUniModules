string = input()
resource_info = {}
while string != "stop":
    quantity = int(input())
    if string not in resource_info:
        resource_info[string] = 0
    resource_info[string] += quantity
    string = input()
for resource, quantity in resource_info.items():
    print(f"{resource} -> {quantity}")
