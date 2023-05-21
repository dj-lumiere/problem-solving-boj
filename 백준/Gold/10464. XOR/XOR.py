# 10464 XOR

from sys import stdin, stdout
from itertools import zip_longest

input = stdin.readline
print = stdout.write


def number_frequency(end: int) -> list[int]:
    if end == 0:
        return [0]
    else:
        digit = end.bit_length()
        num_list = [[0 for i in range(0, digit + 1)], [0 for i in range(0, digit + 1)]]
        # 모든 자릿수의 앞에 0을 붙인 형태로 자릿수를 전부 맞추기
        # 루프를 돌면서 해당하는 자릿수의 갯수를 구하기
        for i in range(1, digit + 1):
            ith_digit = (end // (2 ** (i - 1))) % 2
            for j in range(0, 1 + 1):
                if j < (ith_digit):
                    num_list[j][i - 1] += ((end // (2**i)) + 1) * (2 ** (i - 1))
                elif j == (ith_digit):
                    num_list[j][i - 1] += (
                        (end // (2**i)) * (2 ** (i - 1)) + end % (2 ** (i - 1)) + 1
                    )
                else:
                    num_list[j][i - 1] += (end // (2**i)) * (2 ** (i - 1))
        return num_list[1]


T = int(input())
for _ in range(T):
    M, N = map(int, input().strip().split(" "))
    one_frequency_until_M = number_frequency(M - 1)
    one_frequency_until_N = number_frequency(N)
    one_list = []
    for ith_digit_in_M, ith_digit_in_N in zip_longest(
        one_frequency_until_M, one_frequency_until_N, fillvalue=0
    ):
        one_list.append(ith_digit_in_N - ith_digit_in_M)
    result = sum([2**index * (value % 2) for index, value in enumerate(one_list)])
    print(f"{result}\n")