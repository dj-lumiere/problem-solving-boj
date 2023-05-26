# 15403 Escape Room

from sys import stdin, stdout
from collections import Counter

input = stdin.readline
print = stdout.write

N = int(input())
A = [int(i) for i in input().split(" ")]
count_A = Counter(A)
starting_offset = {}
how_many_numbers_left = N
for index, (number, frequency) in enumerate(
    sorted(count_A.items(), key=lambda x: x[0])
):
    starting_offset[number] = how_many_numbers_left
    how_many_numbers_left -= frequency
result = []
for i in A:
    result.append(starting_offset[i])
    starting_offset[i] -= 1
print(" ".join(map(str, result)))