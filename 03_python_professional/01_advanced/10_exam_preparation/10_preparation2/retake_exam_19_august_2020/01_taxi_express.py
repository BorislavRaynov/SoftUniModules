from collections import deque

customers = deque(input().split(', '))
taxis = deque(input().split(', '))

total_time = 0

while taxis and customers:
    current_customer = int(customers[0])
    current_taxi = int(taxis.pop())

    if current_taxi >= current_customer:
        total_time += current_customer
        customers.popleft()

if len(customers) == 0:
    print('All customers were driven to their destinations')
    print(f"Total time: {total_time} minutes")
else:
    print('Not all customers were driven to their destinations')
    print(f"Customers left: {', '.join(customers)}")
