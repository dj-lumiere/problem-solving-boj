# 4150 피보나치 수


def fib(order: int) -> int:
    last_fib: int = 0
    current_fib: int = 1
    next_fib: int = 1
    for _ in range(1, order):
        last_fib, current_fib, next_fib = current_fib, next_fib, current_fib + next_fib
    return current_fib


n: int = int(input())
print(fib(n))