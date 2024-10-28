from bisect import bisect_left
from itertools import product
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().splitlines())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_009
    t = INF
    answers = []
    cubes = sorted([i ** 3 for i in range(100) if i ** 3 <= 151200])
    tetrahedrals = sorted([i * (i + 1) * (i + 2) // 6 for i in range(100) if i * (i + 1) * (i + 2) // 6 <= 151200])
    cube_tetrahedral = sorted([i + j for i, j in product(cubes, tetrahedrals)])
    cube_tetrahedral.append(INF)
    for _ in range(t):
        n = int(input())
        if n == 0:
            break
        max_sum = cube_tetrahedral[bisect_left(cube_tetrahedral, n)]
        if cube_tetrahedral[bisect_left(cube_tetrahedral, n)] != n:
            max_sum = cube_tetrahedral[bisect_left(cube_tetrahedral, n) - 1]
        answer = max_sum
        answers.append(f"{answer}")
    print(*answers, sep="\n")