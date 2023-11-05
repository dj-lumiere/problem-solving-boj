# D번 - 단체줄넘기
from sys import stdin
from collections import Counter

def input():
    return stdin.readline().strip()

N = int(input())
A = list(map(int, input().split(" ")))
answer = 0
A_counter = Counter(A)
for k, v in A_counter.items():
    if v == 1:
        answer += 1
    else:
        answer += 2
print(answer)