# 2675 문자열 반복
N = int(input())
for _ in range(N):
    a, b = list(map(str, input().split()))
    count = int(a)
    string_list = list(b)
    for i, j in enumerate(b):
        string_list[i] = j * count
    print(*string_list, sep="")