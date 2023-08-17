# 25968 구분구적

from sys import stdin


def input():
    return stdin.readline().strip()


def f(poly, x):
    return sum(v * x ** (2 * i) for i, v in enumerate(poly))


def f_integral(poly, x):
    return sum(v * x ** (2 * i + 1) / (2 * i + 1) for i, v in enumerate(poly))


def find_root(poly):
    start = 0.0
    end = 40.0
    while start + 0.0000005 < end:
        mid = (start + end) / 2
        if f(poly, mid) * poly[0] < 0:
            end = mid
        else:
            start = mid
    return start


def find_area(poly, pieces):
    end = find_root(poly)
    start = -end
    answer = 0.0
    width = 2 * end / pieces
    current_x = start + width / 2
    if pieces > 2000000:
        return abs(f_integral(poly, end)) * 2
    for _ in range(pieces):
        answer += abs(f(poly, current_x)) * width
        current_x += width
    return answer


def main():
    _ = int(input())
    poly = list(map(float, input().split(" ")))
    poly.reverse()
    p = int(input())
    answer = find_area(poly, p)
    print(answer)


main()