price_skumr = float(input())
price_caca = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

price_palamud = price_skumr * 1.6 * palamud_kg
price_safrid = price_caca * 1.8 * safrid_kg
price_midi = 7.5 * midi_kg

total = price_palamud + price_safrid + price_midi
print(f'{total:.2f}')
