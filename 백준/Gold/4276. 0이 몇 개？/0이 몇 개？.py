# 4276 0이 몇개?

from math import log10

def zero_frequency(end:int) -> int:
    if end < 0:
        return 0
    elif end == 0:
        return 1
    else:
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
        num_list[0] += 1
        return num_list[0]

while True:
    A, B = list(map(int, input().split(" ")))
    if A == -1 and B == -1:
        break
    else:
        print(zero_frequency(B)-zero_frequency(A-1))