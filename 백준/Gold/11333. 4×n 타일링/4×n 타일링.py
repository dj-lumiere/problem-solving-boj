# 11333 4×n 타일링

n_list = [1, 3, 13]
for i in range(3331):
    n_list.append((5 * n_list[-1] - 3 * n_list[-2] + n_list[-3]) % 1000000007)
T = int(input())
for _ in range(T):
    N = int(input())
    if N % 3:
        print(0)
    else:
        print(n_list[N // 3])