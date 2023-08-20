count_bitcoin = int(input())
count_cny = float(input())
commission = float(input())

bitcoin_bgn = count_bitcoin * 1168
cny_bgn = count_cny * 0.15 * 1.76
total_eur = (bitcoin_bgn + cny_bgn) / 1.95
final_price = total_eur - (total_eur * commission / 100)

print(f"{final_price:.2f}")
