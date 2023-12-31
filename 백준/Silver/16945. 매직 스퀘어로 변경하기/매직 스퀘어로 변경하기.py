# 16495 매직 스퀘어로 변경하기

from itertools import permutations

A = []
for _ in range(3):
    A.extend(list(map(int, input().split())))

result = 10**18
for numbers in permutations(range(1, 10)):
    if not (
        numbers[0] + numbers[1] + numbers[2]
        == numbers[3] + numbers[4] + numbers[5]
        == numbers[6] + numbers[7] + numbers[8]
        == numbers[0] + numbers[3] + numbers[6]
        == numbers[1] + numbers[4] + numbers[7]
        == numbers[2] + numbers[5] + numbers[8]
        == numbers[0] + numbers[4] + numbers[8]
        == numbers[2] + numbers[4] + numbers[6]
    ):
        continue
    result = min(result, sum(abs(i - j) for i, j in zip(A, numbers)))
print(result)