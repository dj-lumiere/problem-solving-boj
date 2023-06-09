# 1009 분산 처리

pattern = [
    [10],
    [1],
    [6, 2, 4, 8],
    [1, 3, 9, 7],
    [6, 4],
    [5],
    [6],
    [1, 7, 9, 3],
    [6, 8, 4, 2],
    [1, 9],
]

test_cases = int(input())
for _ in range(test_cases):
    a, b = map(int, input().split(" "))
    print(pattern[a % 10][b % (len(pattern[a % 10]))])