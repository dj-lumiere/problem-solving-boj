# 1966 프린터 큐

from collections import deque
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

T = int(input())
for _ in range(T):
    n, m = (int(i) for i in input().split())
    printer_deque = deque(int(i) for i in input().split())
    print_order = 1
    while True:
        be_rotated = False
        for index, value in enumerate(printer_deque):
            if index == 0:
                continue
            elif value > printer_deque[0]:
                be_rotated = True
                break
        if be_rotated:
            m -= 1
            m %= n
            printer_deque.append(printer_deque.popleft())
        elif not be_rotated and m == 0:
            print(f"{print_order}\n")
            break
        else:
            printer_deque.popleft()
            m -= 1
            n -= 1
            m += n
            m %= n
            print_order += 1
