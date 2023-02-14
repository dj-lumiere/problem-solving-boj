# 9527 1의 개수 세기
from math import log2

A, B = list(map(int, input().split(" ")))

def number_frequency(end:int):
    if end == 0:
        return [0,0]
    else:
        num_list = [0 for i in range(0, 1+1)]
        digit = int(log2(end))+1
        # 모든 자릿수의 앞에 0을 붙인 형태로 자릿수를 전부 맞추기
        # 루프를 돌면서 해당하는 자릿수의 갯수를 구하기
        for i in range(1, digit+1):
            ith_digit = (end // (2**(i-1))) % 2
            for j in range(0,1+1):
                if j < (ith_digit):
                    num_list[j] += ((end // (2**i)) + 1) * (2**(i-1))
                elif j == (ith_digit):
                    num_list[j] += (end // (2**i)) * (2**(i-1)) + end % (2**(i-1)) + 1
                else:
                    num_list[j] += (end // (2**i)) * (2**(i-1))
        # 추가적으로 붙은 0에 대해서 보정하기
        for i in range(0, digit):
            num_list[0] -= 2**i
        return num_list

print(number_frequency(B)[1]-number_frequency(A-1)[1])