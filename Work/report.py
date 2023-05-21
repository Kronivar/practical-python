# report.py
#
# Exercise 2.4
import fileparse
import sys
from stock import Stock
import tableformat


def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as filename:
        data = fileparse.parse_csv(filename, 
                                        select=['name', 'shares', 'price'], 
                                        types=[str, int, float])
    
    portfolio = [Stock(s['name'], s['shares'], s['price']) for s in data]
    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as filename:
        prices = fileparse.parse_csv(filename, 
                                     has_headers=False, 
                                     types=[str, float])
    return dict(prices)

def make_report(holdings, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    portfolio = []
    for stock in holdings:
        data = (stock.name, stock.shares, 
                prices[stock.name], 
                prices[stock.name] - stock.price)
        portfolio.append(data)

    return portfolio

def print_report(report, formatter):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(argv):

    if len(argv) != 4:
        raise SystemExit(f"Usage: {argv[0]} portfolio_file prices_file format")
        
    portfolio_report(argv[1], argv[2], argv[3])

if __name__ == '__main__':
    main(sys.argv)
