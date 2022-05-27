pens = int(input())
markers = int(input())
cleaner_ltrs = int(input())
discount = int(input()) / 100

total_no_disc = pens * 5.8 + markers * 7.2 + cleaner_ltrs * 1.2
final = total_no_disc - (total_no_disc * discount)
print(final)
