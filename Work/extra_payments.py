# mortgage.py
#
# Exercise 1.8

# this is wrong program

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
iteration_count = 0
while principal > 0:
    iteration_count += 1
    print(iteration_count)
    if iteration_count<=12:
        payment = payment + 1000
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)