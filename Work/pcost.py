# pcost.py
#
# Exercise 1.27
import csv
import sys
def portfolio_cost(filename):
    with open(filename, 'rt') as file:
        portfolio = csv.reader(file)
        next(portfolio) #skip the header
        sum = 0.0
        for company in portfolio:
            sum += int(company[1]) * float(company[2])
    return sum

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
sum = portfolio_cost(filename)
print('Total cost:', sum)