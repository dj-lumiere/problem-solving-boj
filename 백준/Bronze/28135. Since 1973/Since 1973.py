# 28135 Since 1973

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N = int(input().strip())
answer = 0
next_number = 0
while next_number != N:
    if "50" in str(next_number):
        answer += 2
        next_number += 1
    else:
        answer += 1
        next_number += 1
print(f"{answer}")