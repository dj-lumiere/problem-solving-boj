from itertools import product
from sys import stderr, stdout
from heapq import heappop, heappush

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
    DELTA = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
    INF = 10 ** 18
    MOD = 998_244_353
    t = int(input())
    answers = []
    for hh in range(1, t + 1):
        special_numbers = [1, 2, 4, 6, 12, 16, 22, 28, 36, 52, 58, 66, 82, 106, 112, 136, 166, 178, 256, 306, 336, 352,
                           448, 502, 508, 556, 562, 586, 616, 652, 658, 718, 982, 1018, 1108, 1162, 1192, 1228, 1498,
                           1708, 2002, 2026, 2086, 2686, 2776, 2998, 3136, 3412, 3526, 3592, 4078, 4918, 5008, 5302,
                           5506, 5518, 6112, 6268, 6802, 7126, 7516, 7606, 7918, 7948, 8536, 8542, 8662, 9532, 9748,
                           10312, 10336, 11482, 11578, 13312, 14158, 14548, 14758, 14812, 14968, 19012, 19402, 25228,
                           25366, 28516, 33106, 36676, 43312, 49018, 49612, 52768, 56236, 60352, 65002, 66036, 66082,
                           71866, 75268, 76366, 76756, 79978, 80362, 80932, 96052]
        n = int(input())
        answers.append(len([i for i in special_numbers if i <= n]))
    print(*answers, sep="\n")