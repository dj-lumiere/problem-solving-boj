# 10989 수 정렬하기 3

from sys import stdin, stdout
from array import array

N = int(stdin.readline().strip())
num_list = [0] * 10001
for _ in range(N):
    num_list[int(stdin.readline().strip())] += 1
for i, j in enumerate(num_list):
    for _ in range(j):
        stdout.write(f"{i}\n")