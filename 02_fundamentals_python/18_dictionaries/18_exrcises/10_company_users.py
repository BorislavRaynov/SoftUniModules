info = input()

company_dict = {}

while info != "End":
    company, employee_id = info.split(" -> ")
    if company not in company_dict:
        company_dict[company] = []
        company_dict[company].append(employee_id)
    elif company in company_dict and employee_id not in company_dict[company]:
        company_dict[company].append(employee_id)

    info = input()

for company in company_dict:
    print(f"{company}")
    for value in company_dict[company]:
        print(f"-- {value}")
