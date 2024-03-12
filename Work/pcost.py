import sys
from report import read_portfolio


def portfolio_cost(filename):
    total_cost = 0
    portfolio = read_portfolio(filename)
    for row_num, row in enumerate(portfolio, start=1):
        try:
            shares = int(row['shares'])
            price = float(row['price'])
            total_cost += shares * price
        except ValueError:
            print(f'Row {row_num}: Malformatted row {row}')

    return total_cost


def main(args=['pcost.py', 'Data/portfolio.csv']):
    filename = args[1]

    if len(sys.argv) == 2:
        filename = sys.argv[1]

    cost = portfolio_cost(filename)
    print(f'Total cost: {cost}')
