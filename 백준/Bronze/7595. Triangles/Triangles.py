# 7595 Triangles


def print_triangle(N):
    for i in range(1, N + 1):
        print("*" * i)


while True:
    N = int(input())
    if N == 0:
        break
    print_triangle(N)