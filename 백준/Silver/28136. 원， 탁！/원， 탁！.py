# 28136 원, 탁!

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N = int(input().strip())
A = [int(i) for i in input().split()]
A.append(A[0])
one_tak_count = 0
for (index, value) in enumerate(A):
    if index == 0:
        continue
    elif not value > A[index-1]:
        one_tak_count += 1
print(f"{one_tak_count}")