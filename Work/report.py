# report.py
#
# Exercise 2.4
import csv
from pprint import pprint  
portfolioList= []
def portfolio_cost(filename, stockprices):
    portfolio = []
    total_cost = 0.0
    totalcost_now = 0.0
    with open(filename, 'rt') as file:
        data = csv.reader(file)
        line ='---------'
        headers = next(data)
        print('%10s %10s %10s %10s' %(headers[0], headers[1], headers[2], "change"))
        print('%10s %10s %10s %10s' %(line, line, line, line))
        for d in data:
            portfolioList.append({headers[0]:d[0], headers[1]: int(d[1]), headers[2]:float(d[2])})
            portfolio.append((d[0], int(d[1]),float(d[2])))
            print('%10s %10s %10s %10s' %(d[0], d[1], '$'+stockprices[d[0]], -round(float(d[2]) - float(stockprices[d[0]]),2) ))
    
    for companyname, shares, price in portfolio:
        total_cost += shares * price
        totalcost_now += float(stockprices[companyname]) * shares
    
    return (total_cost, totalcost_now)
def readprices():
    priceDictionary = {}
    with open('Data/prices.csv', 'r') as price:
        pricecsv = csv.reader(price)
        for companyprice in pricecsv:
            if(companyprice):
                priceDictionary[companyprice[0]] = companyprice[1]
    return priceDictionary
priceDict = readprices()       
print("total cost: ", portfolio_cost('Data/portfolio.csv', priceDict))
pprint(portfolioList)
