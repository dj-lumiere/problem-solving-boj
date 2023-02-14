# 3783 세제곱근 1th try


def binary_search(N: int) -> int:
    N = N * 10**90
    start, end = 0, N
    while True:
        mid = (start + end) // 2
        if start == mid or mid == end or mid**3 == N:
            return mid // (10**20)
        elif mid**3 > N:
            end = mid
        elif mid**3 < N:
            start = mid


test_case = int(input())
counter = 0
while True:
    try:
        A = input().lstrip().rstrip()
        if A == "":
            pass
        else:
            x = binary_search(int(A))
            int_part, frac_part = divmod(x, 10**10)
            print(f"{int_part}.{frac_part:0>10}")
            counter += 1
            if counter == test_case:
                break
    except:
        break