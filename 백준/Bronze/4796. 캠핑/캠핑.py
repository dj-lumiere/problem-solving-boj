# 4796 캠핑

i = 1
while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    batch, remainder = divmod(V, P)
    print(f"Case {i}: {batch * L + min(remainder, L)}")
    i += 1