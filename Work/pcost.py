import sys
import csv


def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row_num, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                shares = int(record['shares'])
                price = float(record['price'])
                total_cost += shares * price
            except ValueError:
                print(f'Row {row_num}: Malformatted row {row}')
    return total_cost


filename = 'Data/missing.csv'

if len(sys.argv) == 2:
    filename = sys.argv[1]

cost = portfolio_cost(filename)
print(f'Total cost: {cost}')
