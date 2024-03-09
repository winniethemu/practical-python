with open('Data/portfolio.csv') as file:
    line_num = 0
    total_cost = 0
    for line in file:
        if line_num == 0:
            line_num += 1
            pass
        else:
            [name, shares, price] = line.split(',')
            total_cost += int(shares) * float(price)
    print(f'Total cost {total_cost}')
