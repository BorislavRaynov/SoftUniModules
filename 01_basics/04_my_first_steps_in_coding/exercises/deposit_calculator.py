deposit = float(input())
months = int(input())
interest = float(input())

interest_per_year = deposit * interest / 100
interest_per_month = interest_per_year / 12

total = deposit + interest_per_month * months
print(total)

#сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)