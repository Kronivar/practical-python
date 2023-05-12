# report.py
#
# Exercise 2.4
import csv
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
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
               holdings = (row[0], int(row[1]), float(row[2]))
               portfolio.append(holdings)
            except ValueError:
                print(f"Invalid number for {row[0]}.\nShares: {row[1]}\nPrice: {row[2]}")
                continue
        
    return portfolio

def read_portfolio_dict(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
               record['shares'] = int(record['shares'])
               record['price'] = float(record['price'])
               portfolio.append(record)
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
                continue

    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except ValueError:
                print(f"Invalid price: {row[0]} - {row[1]}")
                continue
            except IndexError:
                print(f"Out of Index")
                continue
        
    return prices

def compute_pf_value(portfolio):
    total_cost = 0.0
    for stock in portfolio:
        total_cost += stock['price'] * stock['shares']
    return total_cost

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
    portfolio = read_portfolio_dict(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

portfolio_report(r'Work\Data\portfolio.csv', r'Work\Data\prices.csv')


