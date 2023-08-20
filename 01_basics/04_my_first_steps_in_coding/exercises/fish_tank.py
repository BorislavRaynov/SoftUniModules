lenght_sm = int(input())
widht_sm = int(input())
h_sm = int(input())
percent_fill = float(input()) / 100

vol = lenght_sm * widht_sm * h_sm / 1000
total_vol = vol - (vol * percent_fill)

print(total_vol)

#Един литър вода се равнява на един кубичен дециметър/ 1л=1 дм3/.

