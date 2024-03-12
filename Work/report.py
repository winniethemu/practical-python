import sys

from fileparse import parse_csv
from stock import Stock


def read_portfolio(filename):
    with open(filename) as file:
        records = parse_csv(file)
        return [
            Stock(
                record['name'],
                record['shares'],
                record['price']
            ) for record in records]


def read_prices(filename):
    with open(filename) as file:
        return dict(parse_csv(file, has_headers=False))


def make_report(portfolio, prices):
    rows = []
    for holding in portfolio:
        name = holding.name
        shares = int(holding.shares)
        purchase_price = float(holding.price)
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


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


def main(args):
    if len(args) < 2:
        args += ['Data/portfolio.csv', 'Data/prices.csv']
    portfolio_report(args[1], args[2])


if __name__ == '__main__':
    main(sys.argv)
