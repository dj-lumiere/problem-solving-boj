# 1351 무한 수열 2

a_dict = dict()
N, P, Q, X, Y = list(map(int, input().split(" ")))

def a(N:int) -> int:
    if N <= 0:
        return 1
    else:
        if N // P - X > 0 and not N // P - X in a_dict:
            a_dict[N//P-X]=a(N//P-X)
        if N // Q - Y > 0 and not N // Q - Y in a_dict:
            a_dict[N//Q-Y]=a(N//Q-Y)
        if N // P - X > 0 and N // Q - Y > 0:
            return a_dict[N//P-X]+a_dict[N//Q-Y]
        elif N // P - X > 0 and N // Q - Y <= 0:
            return a_dict[N//P-X]+1
        elif N // P - X <= 0 and N // Q - Y > 0:
            return 1+a_dict[N//Q-Y]
        elif N // P - X <= 0 and N // Q - Y <= 0:
            return 2

print(a(N))