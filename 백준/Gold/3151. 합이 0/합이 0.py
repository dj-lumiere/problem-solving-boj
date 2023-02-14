# 3151 합이 0

from collections import Counter
from math import factorial
N = int(input())

num_list1 = list(map(int, input().split(" ")))
number_counter = Counter(num_list1)
num_list = list(set(num_list1))
num_list.sort()
N = len(num_list)
coding_ability = 30000
ptr = [0, 0, 0]
count = 0

def nCr(n, r):
    if n < r:
        return 0
    else:
        return factorial(n)//(factorial(r)*factorial(n-r))

count += nCr(number_counter[0], 3)

ptr_j = 0
ptr_k = N - 1
while ptr_j < ptr_k:
    coding_ability_sub = num_list[ptr_j]*2 + num_list[ptr_k]
    if coding_ability_sub > 0:
        ptr_k -= 1
    elif coding_ability_sub < 0:
        ptr_j += 1
    else:
        count += nCr(number_counter[num_list[ptr_j]],2)*nCr(number_counter[num_list[ptr_k]],1)
        ptr_j += 1
        ptr_k -= 1

ptr_j = 0
ptr_k = N - 1
while ptr_j < ptr_k:
    coding_ability_sub = num_list[ptr_j] + num_list[ptr_k]*2
    if coding_ability_sub > 0:
        ptr_k -= 1
    elif coding_ability_sub < 0:
        ptr_j += 1
    else:
        count += nCr(number_counter[num_list[ptr_j]],1)*nCr(number_counter[num_list[ptr_k]],2)
        ptr_j += 1
        ptr_k -= 1

for ptr_i in range(N - 2):
    ptr_j = ptr_i + 1
    ptr_k = N - 1
    while ptr_j < ptr_k:
        coding_ability_sub = num_list[ptr_i] + num_list[ptr_j] + num_list[ptr_k]
        if coding_ability_sub > 0:
            ptr_k -= 1
        elif coding_ability_sub < 0:
            ptr_j += 1
        else:
            count += number_counter[num_list[ptr_i]]*number_counter[num_list[ptr_j]]*number_counter[num_list[ptr_k]]
            ptr_j += 1
            ptr_k -= 1

print(count)