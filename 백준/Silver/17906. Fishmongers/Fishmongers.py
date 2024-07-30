with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    n = int(input())
    m = int(input())
    w = [int(input()) for _ in range(n)]
    fishmongers = [(int(input()), int(input())) for _ in range(m)]
    w.sort()
    fishmongers.sort(key=lambda x: (-x[1], -x[0]))
    max_money = 0
    for x, p in fishmongers:
        for _ in range(x):
            if not w:
                break
            fish_weight = w.pop()
            max_money += fish_weight * p
    print(max_money)
