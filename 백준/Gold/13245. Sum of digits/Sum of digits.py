# 13245 Sum of digits

from math import log10

N = int(input())

def sum_of_digits(end:int):
    num_list = [0 for i in range(0, 9+1)]
    digit = int(log10(end))+1
    # 모든 자릿수의 앞에 0을 붙인 형태로 자릿수를 전부 맞추기
    # 루프를 돌면서 해당하는 자릿수의 갯수를 구하기
    for i in range(1, digit+1):
        ith_digit = (end // (10**(i-1))) % 10
        for j in range(0,9+1):
            if j < (ith_digit):
                num_list[j] += ((end // (10**i)) + 1) * (10**(i-1))
            elif j == (ith_digit):
                num_list[j] += (end // (10**i)) * (10**(i-1)) + end % (10**(i-1)) + 1
            else:
                num_list[j] += (end // (10**i)) * (10**(i-1))
    # 추가적으로 붙은 0에 대해서 보정하기
    for i in range(0, digit):
        num_list[0] -= 10**i
    print(sum([i*j for (i, j) in enumerate(num_list)]))
sum_of_digits(N)