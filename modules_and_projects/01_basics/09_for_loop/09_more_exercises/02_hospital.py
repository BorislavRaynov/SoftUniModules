period_days = int(input())

treated_patients = 0
untreated_patients = 0
init_doctors = 7

for i in range(1, period_days + 1):
    count_patients = int(input())
    if i % 3 == 0:
        if untreated_patients > treated_patients:
            init_doctors += 1
    if count_patients <= init_doctors:
        treated_patients += count_patients
    else:
        treated_patients += init_doctors
        untreated_patients += count_patients - init_doctors

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")