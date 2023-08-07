# 6098 Cruel Math Teacher, II
from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def f_x(x):
    result = 0.0
    for i, v in enumerate(coefficient):
        result += v * x**i
    return result


def f_prime_x(x):
    result = 0.0
    for i, v in enumerate(derivative):
        result += v * x**i
    return result


def next_iteration(initial_value):
    return initial_value - f_x(initial_value) / f_prime_x(initial_value)


D = int(input())
coefficient = [float(input()) for _ in range(D + 1)]
coefficient = [v / coefficient[-1] for v in coefficient]
derivative = [i * v for i, v in enumerate(coefficient) if i > 0]
initial_value = -1000000.0
current_value = [
    initial_value,
    initial_value + 1.5,
]
toggle = False
while abs(current_value[0] - current_value[1]) > 10**-5:
    current_value[not toggle] = next_iteration(current_value[toggle])
    toggle = not toggle
print(f"{int(current_value[toggle] * 1000)}")