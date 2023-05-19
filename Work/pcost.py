# pcost.py
#
# Exercise 1.27
import csv
import sys
import report

def portfolio_cost(filename):
    
    portfolio = report.read_portfolio(filename)

    total_cost = sum([s['shares'] * s['price'] for s in portfolio])
    return total_cost
    
def main(argv):

    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} portfolio_file')

    filename = argv[1]
    cost = portfolio_cost(filename)
    print(f'Total cost: {cost}')

if __name__ == '__main__':
    main(sys.argv)
