import sys

from fileparse import parse_csv
from stock import Stock
from tableformat import HTMLTableFormatter


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
            current_price,
            current_price - purchase_price)
        rows.append(row)
    return rows


def print_report(report_data, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change)
    tuples.
    '''
    formatter.headings(('Name', 'Shares', 'Price', 'Change'))
    for name, shares, price, change in report_data:
        row_data = [name, str(shares), f'${price:0.2f}', f'{change:0.2f}']
        formatter.row(row_data)


def portfolio_report(portfolio_filename, prices_filename):
    '''
    Make a stock report given portfolio and price data files.
    '''
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    formatter = HTMLTableFormatter()
    print_report(report, formatter)


def main(args):
    if len(args) < 2:
        args += ['Data/portfolio.csv', 'Data/prices.csv']
    portfolio_report(args[1], args[2])


if __name__ == '__main__':
    main(sys.argv)
