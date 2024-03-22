import sys

from .fileparse import parse_csv
from .tableformat import create_formatter
from .portfolio import Portfolio


def read_portfolio(filename, **opts):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as file:
        return Portfolio.from_csv(file)


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


def portfolio_report(
        portfolio_filename='Data/portfolio.csv',
        prices_filename='Data/prices.csv',
        fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    formatter = create_formatter(fmt)
    print_report(report, formatter)


def main(args):
    portfolio_report(args[1], args[2], args[3])


if __name__ == '__main__':
    import logging
    logging.basicConfig(
        filename='app.log',
        filemode='w',
        level=logging.WARNING)
    main(sys.argv)
