Z = int(input())
for _ in range(Z):
    n, k = map(int, input().split())
    pattern = list(range(1, n+1))+list(reversed(range(2, n)))
    cycles, k = divmod(k, len(pattern))
    answer = [2*cycles if 2<=i<n else cycles for i in range(n+1)]
    for i, v in enumerate(pattern):
        if i >= k:
            break
        answer[v] += 1
    print(*answer[1:])