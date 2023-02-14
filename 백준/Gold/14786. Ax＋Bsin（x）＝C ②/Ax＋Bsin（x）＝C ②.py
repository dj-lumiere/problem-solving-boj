from math import sin, cos


A, B, C = list(map(int, input().split(" ")))

x_memo = [(C / (A + 1)), 100000.0]


def rec_fact(x):
    return (A * x + B * sin(x) - C) / (A + B * cos(x))

counter = 0
while True:
    x_memo[(counter + 1) % 2] = x_memo[counter % 2] - rec_fact(x_memo[counter % 2])
    counter += 1
    if round(x_memo[0] * (10**10)) == round(x_memo[1] * (10**10)):
        print(x_memo[0])
        break