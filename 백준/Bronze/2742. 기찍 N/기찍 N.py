# 2742 기찍 N
from sys import stdout

N = int(input())
for i in range(N, 0, -1):
    if i != 1:
        stdout.writelines(f"{i}\n")
    else:
        stdout.writelines(f"{i}")