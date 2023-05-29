# 28135 Since 1973

from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def contains_fifty(target: str) -> bool:
    for i in range(len(str(target)) - 1):
        if target[i : i + 2] == "50":
            return True
    return False


N = int(input().strip())
answer = 0
next_number = 0
while next_number != N:
    if contains_fifty(str(next_number)):
        answer += 2
        next_number += 1
    else:
        answer += 1
        next_number += 1
print(f"{answer}")