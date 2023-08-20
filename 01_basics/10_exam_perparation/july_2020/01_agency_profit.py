company_name = input()
adult_tickets = int(input())
kid_tickets = int(input())
net_price_adult = float(input())
service_tax = float(input())


net_price_kid = net_price_adult * 0.30
final_price_kid = net_price_kid + service_tax
final_price_adult = net_price_adult + service_tax
income = adult_tickets * final_price_adult + kid_tickets * final_price_kid

final_income = income * 0.20

print(f"The profit of your agency from {company_name} tickets is {final_income:.2f} lv.")

