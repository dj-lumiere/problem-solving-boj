# 27328 三方比較 (Three-Way Comparison)


def sign(x: int) -> int:
    if not x:
        return 0
    return x // abs(x)


A, B = int(input()), int(input())
print(sign(A - B))