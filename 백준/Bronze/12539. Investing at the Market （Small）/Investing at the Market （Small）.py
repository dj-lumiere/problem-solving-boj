from sys import stderr, stdout

with open(0, "r", encoding="UTF-8") as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = int(input())
    answers = []
    for hh in range(1, t + 1):
        m = int(input())
        prices = [int(input()) for _ in range(12)]
        max_profit = -1
        buy = sell = 0
        for b in range(11):
            for s in range(b + 1, 12):
                units = m // prices[b]
                if units == 0:
                    continue
                profit = (prices[s] - prices[b]) * units
                if profit > max_profit or (profit == max_profit and prices[b] < prices[buy]):
                    if profit > 0:
                        max_profit = profit
                        buy = b
                        sell = s
        if max_profit > 0:
            answer = f"Case #{hh}: {buy + 1} {sell + 1} {max_profit}"
        else:
            answer = f"Case #{hh}: IMPOSSIBLE"
        answers.append(f"{answer}")
    print(*answers, sep="\n")