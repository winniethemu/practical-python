from fileparse import parse_csv


def read_portfolio(filename):
    return parse_csv(filename)


def read_prices(filename):
    return dict(parse_csv(filename, has_headers=False))


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


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


portfolio_file = 'Data/portfoliodate.csv'
prices_file = 'Data/prices.csv'
portfolio_report(portfolio_file, prices_file)
