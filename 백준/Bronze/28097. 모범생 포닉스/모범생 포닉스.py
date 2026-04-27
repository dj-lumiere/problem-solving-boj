# 28097 모범생 포닉스

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N = int(input().strip())
T = [int(i) for i in input().strip().split(" ")]
print(" ".join([str(i) for i in divmod(sum(T) + 8 * N - 8, 24)]))