from itertools import combinations

t = int(input())
answers = []
for hh in range(t):
    a, b, c, d = list(map(int, input().split()))
    daily_plans = list(map(int, input().split()))
    candidates = [d]
    for i in range(5):
        if i == 0:
            for mask in range(1 << 12):
                used_monthly = [mask & (1 << j) != 0 for j in range(12)]
                candidates.append(sum(b if v else a * daily_plans[k] for k, v in enumerate(used_monthly)))
            continue
        for month in combinations(range(10), r=i):
            if any(k - j < 3 for j, k in zip(month, month[1:])):
                continue
            used_quarterly = [False for _ in range(12)]
            for j in month:
                used_quarterly[j:j + 3] = [True] * 3
            not_used_quarterly = [j for j, v in enumerate(used_quarterly) if not v]
            for mask in range(1 << (12 - 3 * i)):
                used_monthly = [mask & (1 << j) != 0 for j in range(12 - 3 * i)]
                candidates.append(
                    sum(b if v else a * daily_plans[not_used_quarterly[k]] for k, v in enumerate(used_monthly)) + i * c)
    answer = min(candidates)
    answers.append(f"#{hh + 1} {answer}")
print(*answers, sep="\n")