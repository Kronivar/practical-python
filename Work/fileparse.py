# fileparse.py
#
# Exercise 3.3

# fileparse.py
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=True):
    '''
    Parse a CSV file into a list of records
    '''

    if not has_headers and select:
        raise RuntimeError("Select argument requires column headers")

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
        for i, row in enumerate(rows, 1):
            
                
            if not row:    # Skip rows with no data
                continue
            
            if select:
                row = [row[i] for i in indices]
            
            if types:
                try:
                    row = [func(x) for func, x in zip(types, row)]
                except ValueError as e:
                    if silence_errors:
                        continue
                    
                    print(f"Row {i}: Couldn't convert {row}")
                    print(f"Row {i}: Reason {e}")

            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)        
            records.append(record)

    return records

# portfolio = parse_csv(r'Work\Data\portfolio.csv', select=['name', 'price'], types=[str, float])
# portfolio = parse_csv(r'Work\Data\prices.csv', select=['name', 'price'], has_headers=False)
# portfolio = parse_csv(r'Work\Data\portfolio.dat', types=[str, int, float], delimiter=' ')
portfolio = parse_csv(r'Work\Data\missing.csv', types=[str, int, float])
print(portfolio)