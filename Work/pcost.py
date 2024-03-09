import gzip


def calculate_cost(file):
    total_cost = 0
    next(file)  # skip header
    for line in file:
        [name, shares, price] = line.split(',')
        try:
            total_cost += int(shares) * float(price)
        except ValueError:
            print(f'Malformatted line: {line}')
    return total_cost


def portfolio_cost(filename):
    if filename.endswith('csv'):
        with open(filename, 'rt') as file:
            return calculate_cost(file)
    elif filename.endswith('gz'):
        with gzip.open(filename, 'rt') as file:
            return calculate_cost(file)
    else:
        pass


cost = portfolio_cost('Data/missing.csv')
print(f'Total cost: {cost}')
