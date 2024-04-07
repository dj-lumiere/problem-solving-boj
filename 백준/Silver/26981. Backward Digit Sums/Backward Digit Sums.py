# 1821 수들의 합 6

from itertools import permutations


def find_bottom_number(number_list) -> int:
    result = [[] for _ in range(len(number_list))]
    result[-1] = number_list
    for i in range(len(number_list) - 1, 0, -1):
        for j in range(i):
            result[i - 1].append(result[i][j] + result[i][j + 1])
    return result[0][0]


N, target = map(int, input().split(" "))
for number_list in permutations(range(1, N + 1), N):
    bottom_number = find_bottom_number(number_list)
    if bottom_number == target:
        print(*number_list)
        break