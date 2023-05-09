# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total = 0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                ticker, shares, price = row
                total += (int(shares) * float(price))
            except ValueError:
                print(f"Invalid number for {ticker}.\nShares: {shares}\nPrice: {price}")
                continue
            
    return total
    
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = r'Work\Data\portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost}')
