import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
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


def make_report(portfolio, prices):
    rows = []
    for holding in portfolio:
        name = holding['name']
        shares = int(holding['shares'])
        purchase_price = float(holding['price'])
        current_price = float(prices[name])
        row = (
            name,
            shares,
            f'${current_price}',
            current_price - purchase_price)
        rows.append(row)
    return rows


def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    for header in headers:
        print(f'{header:>10s}', end=' ')
    print()

    for i in range(4):
        print('----------', end=' ')
    print()

    for r in report:
        print(f'{r[0]:>10s} {r[1]:>10d} {r[2]:>10s} {r[3]:>10.2f}')


portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)
print_report(report)
