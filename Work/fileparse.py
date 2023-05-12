# fileparse.py
#
# Exercise 3.3

# fileparse.py
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        if has_headers:
            headers = next(rows)
        else:
            headers = []

        if select:
            indices = [headers.index(col) for col in select]
            headers = [headers[i] for i in indices]

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            
            if select:
                row = [row[i] for i in indices]
            
            if types:
                row = [func(x) for func, x in zip(types, row)]
            
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            
            records.append(record)

    return records

# portfolio = parse_csv(r'Work\Data\portfolio.csv', select=['name', 'price'], types=[str, float])
portfolio = parse_csv(r'Work\Data\prices.csv', types=[str, float], has_headers=False)
# portfolio = parse_csv(r'Work\Data\portfolio.dat', types=[str, int, float], delimiter=' ')
print(portfolio)