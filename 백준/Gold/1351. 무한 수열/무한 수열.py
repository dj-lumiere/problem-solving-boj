a_dict = dict()
a_dict[0] = 1
N, P, Q = list(map(int, input().split(" ")))

def a(N:int) -> int:
    if N == 0:
        return 1
    else:
        if not N // P in a_dict:
            a_dict[N//P]=a(N//P)
        if not N // Q in a_dict:
            a_dict[N//Q]=a(N//Q)
        return a_dict[N//P]+a_dict[N//Q]

print(a(N))