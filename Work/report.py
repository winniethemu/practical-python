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


def make_report(portfolio, prices):
    rows = []
    for holding in portfolio:
        name = holding['name']
        shares = holding['shares']
        purchase_price = holding['price']
        current_price = prices[name]
        row = (name, shares, current_price, current_price - purchase_price)
        rows.append(row)
    return rows


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

for r in report:
    print(r)
