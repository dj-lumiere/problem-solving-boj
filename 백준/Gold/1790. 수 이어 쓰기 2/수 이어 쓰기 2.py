# 1790 수 이어 쓰기 2
from math import log10, ceil
N, k = list(map(int, input().split(" ")))
number_length = [0]
for i in range(1, 9+1):
    number_length.append(number_length[i-1]+(10**i-10**(i-1))*i)
def length_N(N):
    return number_length[int(log10(N))]+(N-10**int(log10(N))+1)*(int(log10(N))+1)
if k > length_N(N):
    print(-1)
else:
    for i in range(9):
        if number_length[i] < k <= number_length[i+1]:
            kth_digit = 10 ** i - 1 + ceil((k - number_length[i]) / (i + 1))
            letter = length_N(kth_digit) - k
            kth_number = (kth_digit // 10 ** letter) % 10
            print(kth_number)
            break