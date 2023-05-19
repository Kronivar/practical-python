# report.py
#
# Exercise 2.4
import csv
import fileparse
import sys
from pprint import pprint

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


def read_portfolio(filename):

    with open(filename) as filename:
        portfolio = fileparse.parse_csv(filename, 
                                        select=['name', 'shares', 'price'], 
                                        types=[str, int, float])
    
    return portfolio

def read_prices(filename):

    with open(filename) as filename:
        prices = fileparse.parse_csv(filename, 
                                     has_headers=False, 
                                     types=[str, float])
    return dict(prices)

def make_report(holdings, prices):
    portfolio = []
    for stock in holdings:
        data = (stock['name'], stock['shares'], 
                prices[stock['name']], 
                prices[stock['name']] - stock['price'])
        portfolio.append(data)

    return portfolio

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(("-" * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

def main(argv):

    if len(argv) != 3:
        raise SystemExit(f"Usage: {argv[0]} portfolio_file prices_file")
        
    portfolio_report(argv[1], argv[2])

if __name__ == '__main__':
    main(sys.argv)
