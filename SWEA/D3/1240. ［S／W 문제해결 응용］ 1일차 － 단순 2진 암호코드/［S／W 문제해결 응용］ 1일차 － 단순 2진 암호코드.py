from itertools import product

t = int(input())
answers = []
decoder = {v: i for i, v in enumerate([13, 25, 19, 61, 35, 49, 47, 59, 55, 11])}
for hh in range(1, t + 1):
    n, m = map(int, input().split())
    grid = [list(map(int, input())) for _ in range(n)]
    code = []
    for y, x in product(range(n), range(m - 55)):
        subgrid = [grid[y][x + x2] for x2 in range(56)]
        code_candidate = [decoder.get(sum(v << (6 - i) for i, v in enumerate(v2)), -1) for v2 in
                          zip(*(subgrid[j::7] for j in range(7)))]
        if all(v != -1 for v in code_candidate) and (sum(code_candidate[::2]) * 3 + sum(
                code_candidate[1::2])) % 10 == 0:
            code = code_candidate
            break
    answer = sum(code)
    answers.append(f"#{hh} {answer}")
print(*answers, sep="\n")