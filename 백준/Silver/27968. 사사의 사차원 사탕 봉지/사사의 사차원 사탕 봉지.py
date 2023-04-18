# J번

from bisect import bisect_left
from sys import stdin, stdout

N, M = map(int, stdin.readline().strip().split())
A = list(map(int, stdin.readline().strip().split(" ")))
A_accumulated_sum = [0]
for i in range(M):
    A_accumulated_sum.append(A_accumulated_sum[-1] + A[i])
for _ in range(N):
    B = int(stdin.readline().strip())
    candy_pull_count = bisect_left(A_accumulated_sum, B)
    if candy_pull_count > M:
        stdout.write("Go away!\n")
    else:
        stdout.write(f"{candy_pull_count}\n")
