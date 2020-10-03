# bounce.py
#
# Exercise 1.5
height = 100
no_of_bounce = 10
bounced_back = 3/5
initial_bounce = 1

while initial_bounce <= no_of_bounce:
    bounced = round(height * bounced_back, 4)
    print(bounced)
    height = bounced
    initial_bounce += 1