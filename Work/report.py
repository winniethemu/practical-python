import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            shares = int(row[1])
            price = float(row[2])
            portfolio.append((row[0], shares, price))
    return portfolio
