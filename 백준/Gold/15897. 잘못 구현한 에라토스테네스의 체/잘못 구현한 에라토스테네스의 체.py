# 15897 잘못 구현한 에라토스테네스의 체

from math import ceil
from collections import Counter
N = int(input())
# ceil(N//i)의 합
# 1을 제외한 sqrt(N)까지의 정수에 대하여
# i의 빈도는 ceil(N/i)번
# ceil(N/i)의 빈도는 1번
# i와 ceil(N/i)를 제외한 정수는 빈도 0번
count = 0
ceil_Ni = []
for i in range(1, ceil(N**0.5)+1):
    ceil_Ni.append(ceil(N/i))
ceil_Ni_difference = []
for i, j in enumerate(ceil_Ni):
    if i == 0:
        ceil_Ni_difference.append(1)
    else:
        ceil_Ni_difference.append(ceil_Ni[i-1]-j)
for i, (j, k) in enumerate(zip(ceil_Ni, ceil_Ni_difference)):
    count += j + (i+1)*k
if ceil_Ni[-1] != len(ceil_Ni):
    count -= ceil_Ni[-1] + len(ceil_Ni)
else:
    count -= len(ceil_Ni)
print(count)