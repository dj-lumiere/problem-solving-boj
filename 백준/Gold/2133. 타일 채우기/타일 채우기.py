# 2133 타일 채우기

N = int(input())
if N % 2:
    print(0)
else:
    N //= 2
    # a(1) = 3, a(2) = 5
    # a(n+2) = 3*a(n+1)+2*S(n)
    n_list = [1, 3]
    if N >= 2:
        for i in range(N+1):
            if i >= 2:
                n_list.append(3 * n_list[-1] + 2 * sum(n_list[:-1]))
        print(n_list[N])
    else:
        print(n_list[N])