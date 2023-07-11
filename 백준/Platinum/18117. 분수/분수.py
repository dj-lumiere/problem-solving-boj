# 18117 분수


def find_digits(a: int, b: int, x: int, y: int) -> str:
    result = ""
    for i in range(x, y):
        result_sub = ((a * pow(10, i - 1, b) % b) * 10) // b
        result += str(result_sub)
    return result


t = int(input())
for _ in range(t):
    a, b = map(int, input().split(" "))
    i, n = map(int, input().split(" "))
    print(find_digits(a, b, i, i + n))