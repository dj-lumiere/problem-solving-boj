N = int(input())

def sol(N : int):
    if N == 0:
        return 1
    else:
        return N * sol(N-1)

print(sol(N))