# 3460 이진수

T = int(input())
for _ in range(T):
    n = int(input())
    bin_n = list(map(int, (bin(n)[2:])[::-1]))
    one_place = [i for i, v in enumerate(bin_n) if v]
    print(*one_place)