# 28065 SW 수열 구하기

from math import floor, ceil
from sys import stdin, stdout
from itertools import zip_longest

input = stdin.readline
print = stdout.write

# 반절로 나눈 뒤 사이사이에 껴넣기

N = int(input())
answer_even_index = list(range(N, ceil(N / 2) - 1, -1))
answer_odd_index = list(range(1, floor(N / 2) + 1))
answer = []
for even, odd in zip_longest(answer_even_index, answer_odd_index, fillvalue=0):
    answer.append(even)
    answer.append(odd)
if N % 2:
    answer.pop()
else:
    answer.pop()
    answer.pop()
print(" ".join(map(str, answer)))