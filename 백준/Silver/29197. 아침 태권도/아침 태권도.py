# 29197 아침 태권도

from math import gcd


def compress_dot(x: int, y: int) -> tuple[int, int]:
    if y == 0 and x > 0:
        return (1, 0)
    elif y == 0 and x < 0:
        return (-1, 0)
    compression_factor = gcd(x, y)
    return (x // compression_factor, y // compression_factor)


student_count_same_gradient = {}
N = int(input())
for _ in range(N):
    x, y = map(int, input().split(" "))
    x, y = compress_dot(x, y)
    student_count_same_gradient[(x, y)] = student_count_same_gradient.get((x, y), 0) + 1
print(f"{len(student_count_same_gradient)}")