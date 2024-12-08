from collections import deque
from sys import stderr, stdout


def precise_round(numerator: int, denominator: int, precision: int) -> str:
    scaling_factor = 10 ** precision
    raw_value = numerator * scaling_factor * 10 // denominator
    rounded_value = (raw_value + 5) // 10
    integer_part, fractional_part = divmod(rounded_value, scaling_factor)
    return f"{integer_part}.{str(fractional_part).zfill(precision)}"


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
    positions = {'Q': (0, 0), 'W': (2, 0), 'E': (4, 0), 'R': (6, 0), 'T': (8, 0), 'Y': (10, 0), 'U': (12, 0), 'I': (
    14, 0), 'O'     : (16, 0), 'P': (18, 0), 'A': (1, 1), 'S': (3, 1), 'D': (5, 1), 'F': (7, 1), 'G': (9, 1), 'H': (
    11, 1), 'J'     : (13, 1), 'K': (15, 1), 'L': (17, 1), 'Z': (2, 2), 'X': (4, 2), 'C': (6, 2), 'V': (8, 2), 'B': (
    10, 2), 'N'     : (12, 2), 'M': (14, 2)}
    adjacency = {k: [] for k in positions}
    for k1, v1 in positions.items():
        for k2, v2 in positions.items():
            dx = abs(v1[0] - v2[0])
            dy = abs(v1[1] - v2[1])
            if (dx == 2 and dy == 0) or (dx == 1 and dy == 1):
                adjacency[k1].append(k2)
    distances = {k: {} for k in positions}
    for k in positions:
        q = deque()
        q.append((k, 0))
        visited = set()
        visited.add(k)
        while q:
            current, dist = q.popleft()
            distances[k][current] = dist
            for neighbor in adjacency[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, dist + 1))
    t = int(input())
    answers = []
    for _ in range(t):
        s = input()
        total = 1
        prev = s[0]
        for c in s[1:]:
            total += distances[prev][c] * 2 + 1
            prev = c
        answers.append(f"{total}")
    print(*answers, sep="\n")