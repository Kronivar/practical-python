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
        for row in rows:
            try:
               holdings = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])} 
               portfolio.append(holdings)
            except ValueError:
                print(f"Invalid number for {row[0]}.\nShares: {row[1]}\nPrice: {row[2]}")
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



portfolio_dict = read_portfolio_dict(r'Work\Data\portfolio.csv')
total_cost = compute_pf_value(portfolio_dict)

prices = read_prices(r'Work\Data\prices.csv')

current_pf_value = 0.0
for stock in portfolio_dict:
    current_pf_value += stock['shares'] * prices[stock['name']]

print(f"Cost basis: {total_cost:.2f}\nCurrent portfolio value: {current_pf_value}\nTotal gain/loss: {current_pf_value - total_cost}")