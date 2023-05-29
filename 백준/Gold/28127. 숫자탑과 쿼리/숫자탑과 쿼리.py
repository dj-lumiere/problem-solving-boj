# 28127 숫자탑과 쿼리

from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def quadratic_equation(a, b, c) -> float:
    return (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)


def floor_finder(a, d, x) -> int:
    # k층까지의 모든 블록 갯수 합 : S(k)=(d/2)k**2+(a-d/2)*k=x
    # dk**2+(2a-d)*k=2x
    return int(quadratic_equation(d, 2 * a - d, -2 * x))


def blocks_from_nth_floor(a, d, n) -> int:
    return (d * n**2 + (2 * a - d) * n) // 2


def blocks_in_nth_floor(a, d, n) -> int:
    return a + d * (n - 1)


Q = int(input())
for _ in range(Q):
    a, d, x = (int(i) for i in input().split(" "))
    floor = floor_finder(a, d, x)
    residue = x - blocks_from_nth_floor(a, d, floor)
    if residue == 0:
        residue += blocks_in_nth_floor(a, d, floor)
        floor -= 1
    floor += 1
    print(f"{floor} {residue}\n")