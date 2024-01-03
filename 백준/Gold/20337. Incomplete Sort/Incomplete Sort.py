# 20337 Incomplete Sort
from random import randint


def sort_subarray(A, index):
    temp = []
    for i in index:
        temp.append(A[i - 1])
    temp.sort()
    for i, v in enumerate(index):
        A[v - 1] = temp[i]


N = int(input())
A = list(map(int, input().split()))
print(3)
first_sort = set()
for i, v in enumerate(A, start=1):
    if 3 * N // 4 < i <= 4 * N // 4 or 3 * N // 4 < v <= 4 * N // 4:
        first_sort.add(i)
if len(first_sort) != N // 2:
    while len(first_sort) < N // 2:
        index = randint(1, N)
        if index in first_sort:
            continue
        first_sort.add(index)
print(*sorted(first_sort))
sort_subarray(A, sorted(first_sort))
second_sort = set()
for i, v in enumerate(A, start=1):
    if 2 * N // 4 < i <= 3 * N // 4 or 2 * N // 4 < v <= 3 * N // 4:
        second_sort.add(i)
if len(second_sort) != N // 2:
    while len(second_sort) < N // 2:
        index = randint(1, N)
        if index in second_sort:
            continue
        second_sort.add(index)
print(*sorted(second_sort))
sort_subarray(A, sorted(second_sort))
print(*range(1, N // 2 + 1))