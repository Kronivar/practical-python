# mortgage.py
#
# Exercise 1.7-1.11

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

no_of_payments = 1
extra_payment_start_month = int(input("Please input the month at which extra payments will start: "))
extra_payment_end_month = int(input("Please input the month at which extra payments will stop: "))
extra_payment = float(input("Please input the extra payment amount: "))

while principal > 0:
    while no_of_payments >= extra_payment_start_month and no_of_payments <= extra_payment_end_month:
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
        no_of_payments += 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    no_of_payments += 1  
    if principal <= 0:
        total_paid += principal
        principal = 0  
    print(f"{no_of_payments} {total_paid:.2f} {principal:.2f}")

print('Total paid', round(total_paid, 2))