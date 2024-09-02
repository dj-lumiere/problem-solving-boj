from itertools import product, chain, permutations, combinations

INF = 10 ** 18
MOD = 1_000_000_000
t = int(input())
answers = []
for hh in range(1, t + 1):
    s, y = map(int, input().split())
    s2 = list(map(int, str(s)))
    target = int("".join(map(str, sorted(s2, reverse=True))))
    target_list = sorted(s2, reverse=True)
    index = 0
    max_possible = [False for _ in range(11)]
    max_values = [-INF for _ in range(11)]
    max_possible_min_attempts = INF
    for i in range(1, max(3, len(s2))):
        for moves in product(combinations(range(len(s2)), r=2), repeat=i):
            s3 = s2[:]
            for j, k in moves:
                s3[j], s3[k] = s3[k], s3[j]
            s4 = sum(v * 10 ** (len(s3) - 1 - i) for i, v in enumerate(s3))
            if s4 == target:
                max_possible[i] = True
                for j in range(i, 11, 2):
                    max_possible[j] = True
                    max_values[j] = target
                max_possible_min_attempts = min(max_possible_min_attempts, i)
            else:
                max_values[i] = max(max_values[i], s4)
                for j in range(i, 11, 2):
                    max_values[j] = max(max_values[j], s4)
    answer = max_values[y]
    answers.append(f"#{hh} {answer}")
print(*answers, sep="\n")