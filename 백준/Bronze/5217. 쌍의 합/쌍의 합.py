# 5217 쌍의 합

t = int(input())
for _ in range(t):
    n = int(input())
    print(
        f'Pairs for {n}: {", ".join(map(lambda x:f"{x[0]} {x[1]}", [(i,n-i) for i in range(1, n+1) if i < n-i]))}'
    )