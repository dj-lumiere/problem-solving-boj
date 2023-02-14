# 12865 평범한 배낭
N, K = list(map(int, input().split(" ")))
item_list = []
for _ in range(N):
    W, V = map(int, input().split(" "))
    item_list.append((W, V))
value_list = [[0 for i in range(K + 1)] for j in range(N + 1)]


def zero_one_knapsack() -> int:
    for i in range(N + 1):
        for c in range(K + 1):
            if i == 0 or c == 0:
                continue
            elif item_list[i - 1][0] <= c:
                value_list[i][c] = max(
                    item_list[i - 1][1] + value_list[i - 1][c - item_list[i - 1][0]],
                    value_list[i - 1][c],
                )
            else:
                value_list[i][c] = value_list[i - 1][c]
    return value_list[-1][-1]


print(zero_one_knapsack())