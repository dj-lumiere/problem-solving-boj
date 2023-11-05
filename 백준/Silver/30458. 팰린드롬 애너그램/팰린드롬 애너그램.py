# 30458 팰린드롬 애너그램
from sys import stdin


def input():
    return stdin.readline().strip()


N = int(input())
S = list(input())
S_left_counter = dict()
S_right_counter = dict()
possible = True
for i in "abcdefghijklmnopqrstuvwxyz":
    S_left_counter[i] = 0
    S_right_counter[i] = 0
for i in range(N // 2):
    S_left_counter[S[i]] += 1
    S_right_counter[S[-i - 1]] += 1

for i in "abcdefghijklmnopqrstuvwxyz":
    if S_left_counter[i] & 1 != S_right_counter[i] & 1:
        possible = False
        break
print("Yes" if possible else "No")