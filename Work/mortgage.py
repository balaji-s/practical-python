# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment = 1000

while principal > 0:
    if months < 12:
        payment1 = payment + 1000
    else:
        payment1 = payment
    principal = principal * (1+rate/12) - payment1
    total_paid = total_paid + payment1
    months += 1

print('Total paid', total_paid)