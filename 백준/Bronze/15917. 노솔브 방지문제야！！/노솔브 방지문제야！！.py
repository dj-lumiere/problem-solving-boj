# 15917 노솔브 방지문제야!!
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

Q = int(input())
for _ in range(Q):
    a = int(input())
    print(f"{int(a&(-a)==a)}\n")