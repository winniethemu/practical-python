principal = 500000.0
rate = 0.05
regular_payment = 2684.11
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
total_paid = 0.0
month = 0

while principal > 0:
    month += 1
    if extra_payment_start_month <= month and month <= extra_payment_end_month:
        payment = regular_payment + extra_payment
    else:
        payment = regular_payment
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    print(month, round(total_paid, ndigits=2), round(principal, ndigits=2))

print('Total payment', total_paid)
print('Total month', month)
