from os import write

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep=" ", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    for hh in range(t):
        n = int(input())
        numbers = [0] + [int(input()) for _ in range(n)]
        index_minmax = {}
        for i, v in enumerate(numbers):
            if i == 0:
                continue
            if v not in index_minmax:
                index_minmax[v] = [i, i]
                continue
            index_minmax[v][1] = max(index_minmax[v][1], i)
        sum_pair_count = {}
        numbers_sum = []
        for i, v in enumerate(numbers):
            if i == 0:
                numbers_sum.append(0)
                continue
            numbers_sum.append(numbers_sum[-1]+v)
        for k, (v1, v2) in index_minmax.items():
            max_pair = numbers_sum[v2] - numbers_sum[v1-1]
            if max_pair not in sum_pair_count:
                sum_pair_count[max_pair] = 0
            sum_pair_count[max_pair] += 1
        answer = f"{max(sum_pair_count.keys())} {sum_pair_count[max(sum_pair_count.keys())]}"
        answers.append(f"{answer}")
    print(*answers,end="\n")