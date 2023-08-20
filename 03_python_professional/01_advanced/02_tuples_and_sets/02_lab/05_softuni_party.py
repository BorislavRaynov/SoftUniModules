count_guests = int(input())

vip_guests = set()
regular_guests = set()

for g in range(count_guests):
    res_codes = input()
    if res_codes[0].isdigit():
        vip_guests.add(res_codes)
    else:
        regular_guests.add(res_codes)


visitors = input()
while visitors != "END":
    if visitors in vip_guests:
        vip_guests.remove(visitors)
    elif visitors in regular_guests:
        regular_guests.remove(visitors)
    visitors = input()

print(len(vip_guests) + len(regular_guests))
if len(vip_guests) > 0:
    print("\n".join(sorted(vip_guests)))
if len(regular_guests) > 0:
    print("\n".join(sorted(regular_guests)))
