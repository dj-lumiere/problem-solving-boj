answers = []
INF = 10 ** 18
MOD = 1_000_000_000
t = 10
for hh in range(t):
    n = int(input())
    node = ["" for _ in range(201)]
    graph = [[] for _ in range(201)]
    for _ in range(n):
        x, y, *nodes = input().split()
        node[int(x)] = y
        for i in nodes:
            graph[int(x)].append(int(i))
            graph[int(i)].append(int(x))
    leaves = [i for i, v in enumerate(graph) if len(v) == 1]
    answer = int(all("0" <= i <= "9" for i in map(lambda x: node[x], leaves)))
    answers.append(f"#{hh + 1} {answer}")
print(*answers, sep="\n")
