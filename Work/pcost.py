import sys
from report import read_portfolio


def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = read_portfolio(filename)
    return portfolio.total_cost


def main(args):
    filename = 'Data/portfolio.csv'

    if len(sys.argv) == 2:
        filename = sys.argv[1]

    cost = portfolio_cost(filename)
    print(f'Total cost: {cost}')


if __name__ == '__main__':
    main(sys.argv)
