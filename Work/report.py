import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            record = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2]),
            }
            portfolio.append(record)
    return portfolio


def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) > 0:
                name, price = row
                prices[name] = price
    return prices
