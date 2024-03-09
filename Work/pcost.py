with open('Data/portfolio.csv') as file:
    total_cost = 0
    next(file)  # skip header
    for line in file:
        [name, shares, price] = line.split(',')
        total_cost += int(shares) * float(price)
    print(f'Total cost {total_cost}')
