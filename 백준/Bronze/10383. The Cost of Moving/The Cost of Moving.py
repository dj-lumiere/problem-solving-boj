from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    INF = 10 ** 18
    t = INF
    answers = []
    site = 1
    for hh in range(t):
        n = int(input())
        if n == 0:
            break
        products = []
        while len(products) < n:
            word = input()
            if word is not None:
                products.append(word)
            else:
                break
        sorted_products = sorted(products)
        total = 0
        for i in range(n):
            total += abs(i - sorted_products.index(products[i]))
        answer = f"Site {site}: {total}"
        site += 1
        answers.append(f"{answer}")
    print(*answers, sep="\n")