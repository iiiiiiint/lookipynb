def deal(max_weights, weights, quantities, profit_sort):
    for idx in profit_sort:
        if quantities[idx] > 0 and weights[idx] <= max_weights:
            count = max_weights // weights[idx]
            max_weights = max_weights % weights[idx]
            quantities[idx] -= count
            return idx, count, max_weights, quantities
    return -1, 0, max_weights, quantities

if __name__ == '__main__':
    with open('assignment_3_Q3_input.txt', 'r') as f:
        lines = f.readlines()
    max_weights, weights, quantities, profits = lines
    max_weights = int(max_weights)
    weights = list(map(int, weights.strip().split(' ')))
    quantities = list(map(int, quantities.strip().split(' ')))
    profits = list(map(int, profits.strip().split(' ')))

    single_profits = []
    for weight, profit in zip(weights, profits):
        single_profits.append(profit/weight)
    profit_sort = sorted(range(len(single_profits)), key = lambda x:single_profits[x], reverse=True)
    single_profits, profit_sort
    
    all_profit = 0
    results = []
    while True:
        if max_weights <= 0:
            break
        idx, count, max_weights, quantities = deal(max_weights, weights, quantities, profit_sort)
        if idx == -1:
            break
        else:
            results.append((weights[idx], quantities[idx]+count, profits[idx], count))
            all_profit += profits[idx] * count
    
    with open('assignment_3_Q3_output.txt', 'w') as f:
        f.write(str(all_profit)+'\n')
        for result in results:
            f.write(' '.join(map(str, result))+'\n')