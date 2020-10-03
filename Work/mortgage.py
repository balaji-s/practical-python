# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
months = 1

while principal > 0:
    if months >= extra_payment_start_month and extra_payment_start_month <= extra_payment_end_month:
        payment1 = payment + extra_payment
        extra_payment_start_month += 1
    else:
        payment1 = payment
    to_be_paid = principal * (1+rate/12) - payment1
    if(to_be_paid < 0):
        principal = 0
    else:
        principal = to_be_paid        
    total_paid = total_paid + payment1
    print(months, total_paid, principal)
    if(principal > 0): months += 1

print('Total paid', total_paid, "Months: ",months)