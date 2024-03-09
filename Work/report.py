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
                prices[name] = float(price)
    return prices


initial_value = 0
current_value = 0

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

for holding in portfolio:
    initial_price = holding['price']
    initial_value += initial_price * holding['shares']
    current_price = prices[holding['name']]
    current_value += current_price * holding['shares']

print('Initial value', initial_value)
print('Current value', current_value)
print('Gain', current_value - initial_value)
