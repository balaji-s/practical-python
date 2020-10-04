# pcost.py
#
# Exercise 1.27
import csv
def portfolio_cost(filename):
    with open(filename, 'rt') as file:
        portfolio = csv.reader(file)
        next(portfolio) #skip the header
        sum = 0.0
        for company in portfolio:
            sum += int(company[1]) * float(company[2])
    return sum

sum = portfolio_cost('Data/portfolio.csv')
print('Total cost:', sum)