principal = 500000.0
rate = 0.05
regular_payment = 2684.11
extra_payment = regular_payment + 1000
total_paid = 0.0
month = 0

while principal > 0:
    month += 1
    payment = extra_payment if month <= 12 else regular_payment
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total payment', total_paid)
print('Total month', month)
