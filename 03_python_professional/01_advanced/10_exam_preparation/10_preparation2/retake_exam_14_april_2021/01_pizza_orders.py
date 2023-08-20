from collections import deque

orders = deque(map(int, input().split(', ')))
employees = deque(map(int, input().split(', ')))

pizzas_made = 0

while orders and employees:
    current_order = orders[0]
    current_employee = employees[-1]

    if current_order <= 0 or current_order > 10:
        orders.popleft()

    elif current_order <= current_employee:
        pizzas_made += current_order
        orders.popleft()
        employees.pop()

    elif current_order > current_employee:
        pizzas_made += current_employee
        orders[0] -= current_employee
        employees.pop()

if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas_made}")
    print(f"Employees: {', '.join(map(str, employees))}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join((map(str, orders)))}")
