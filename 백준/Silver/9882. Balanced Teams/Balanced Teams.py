import os
from itertools import combinations


def difference(teams):
    max_skill = max(sum(i) for i in teams)
    min_skill = min(sum(i) for i in teams)
    return max_skill - min_skill


# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        numbers = [int(input()) for _ in range(12)]
        eprint(numbers)
        group_difference = []
        for group1 in combinations(range(12), r=3):
            candidate = [j for j in range(12) if j not in group1]
            for group2 in combinations(candidate, r=3):
                candidate2 = [j for j in candidate if j not in group2]
                for group3 in combinations(candidate2, r=3):
                    group4 = [j for j in candidate2 if j not in group3]
                    teams = [[numbers[x] for x in v] for v in [group1, group2, group3, group4]]
                    group_difference.append(difference(teams))
        answers[i] = f"{min(group_difference)}"
    print(answers)