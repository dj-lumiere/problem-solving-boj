# 1793 타일링

from sys import stdin


# 공백이 될 때까지 아이템을 불러오는 함수
def loading_list() -> list[int]:
    string_list = []
    while True:
        string_element = stdin.readline().rstrip()
        if not string_element:
            return string_list
        else:
            string_list.append(int(string_element))


def tiling_number(n: int) -> int:
    # f(n) = 2*f(n-2)+f(n-1)
    memo = [1, 1]
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        for i in range((n - 2) + 1):
            memo[i % 2] = 2 * memo[(i - 2) % 2] + memo[(i - 1) % 2]
        return memo[n % 2]


def main():
    queries = loading_list()
    for i in queries:
        print(tiling_number(i))


main()
