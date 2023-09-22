# 9299 Math Tutoring


def find_derivative(polynomial: list[int]) -> list[int]:
    polynomial.pop()
    result = []
    for i, v in enumerate(reversed(polynomial), start=1):
        result.append(i * v)
    return result[::-1]


T = int(input())
for i in range(1, T + 1):
    _, *polynomial = map(int, input().split(" "))
    result = find_derivative(polynomial)
    print(f"Case {i}: {len(result)-1} {' '.join(map(str, result))}")