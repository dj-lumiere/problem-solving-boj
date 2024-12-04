from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        N_orders = int(input())
        buy_orders = {}
        sell_orders = {}
        current_price = 10000
        for _ in range(N_orders):
            p_i = int(input())
            x_i = int(input())
            f_i = int(input())
            if f_i == 1:
                if p_i in sell_orders and sell_orders[p_i] >= 1:
                    bought = min(sell_orders[p_i], x_i)
                    sell_orders[p_i] -= bought
                    current_price = p_i
                    if x_i > bought:
                        buy_orders[p_i] = buy_orders.get(p_i, 0) + (x_i - bought)
                else:
                    buy_orders[p_i] = buy_orders.get(p_i, 0) + x_i
            elif f_i == -1:
                if p_i in buy_orders and buy_orders[p_i] >= 1:
                    sold = min(buy_orders[p_i], x_i)
                    buy_orders[p_i] -= sold
                    current_price = p_i
                    if x_i > sold:
                        sell_orders[p_i] = sell_orders.get(p_i, 0) + (x_i - sold)
                else:
                    sell_orders[p_i] = sell_orders.get(p_i, 0) + x_i
        answer = current_price
        answers.append(f"{answer}")
    print(*answers, sep="\n")