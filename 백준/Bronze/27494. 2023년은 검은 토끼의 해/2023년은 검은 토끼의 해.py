# 27494 2023년은 검은 토끼의 해

from sys import stdin, stdout

input = stdin.readline
print = stdout.write
x = int(input())
answer = 0
for i in range(1, x + 1):
    digit_list = list(str(i))
    digit_found = [False, False, False, False]
    for digit in digit_list:
        if digit == "2" and not any(digit_found):
            digit_found[0] = True
        if digit == "0" and digit_found[0]:
            digit_found[1] = True
        if digit == "2" and digit_found[0] and digit_found[1]:
            digit_found[2] = True
        if digit == "3" and digit_found[0] and digit_found[1] and digit_found[2]:
            digit_found[3] = True
    if all(digit_found):
        answer += 1
print(f"{answer}")