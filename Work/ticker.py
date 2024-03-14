import csv

from follow import follow
from report import read_portfolio
from tableformat import create_formatter


def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row


def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    #  rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows


def ticker(portfile, logfile, fmt):
    portfolio = read_portfolio(portfile)
    lines = follow(logfile)
    formatter = create_formatter(fmt)
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)

    formatter.headings(['Name', 'Price', 'Change'])
    for row in rows:
        formatter.row(row.values())


if __name__ == '__main__':
    lines = follow('Data/stocklog.csv')
    portfolio = read_portfolio('Data/portfolio.csv')
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)
    for row in rows:
        print(row)
