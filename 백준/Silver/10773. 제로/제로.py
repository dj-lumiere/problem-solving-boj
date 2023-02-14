from sys import stdin

K = int(input())

def zero_n(n: int) -> None:
    stack = []
    while n:
        n -= 1
        element = int(stdin.readline().rstrip())
        if not element:
            stack.pop()
        else:
            stack.append(element)
    print(sum(stack))

zero_n(K)