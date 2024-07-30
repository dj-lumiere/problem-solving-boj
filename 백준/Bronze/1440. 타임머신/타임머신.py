from itertools import permutations

d = list(map(int, input().split(":")))
answer = []
limit = [range(1, 13), range(60), range(60)]
for i in permutations(range(3)):
    clock = [0, 0, 0]
    for a, b in enumerate(i):
        clock[b] = d[a]
    if all(i in j for i, j in zip(clock, limit)):
        answer.append(tuple(clock))
print(len(answer))