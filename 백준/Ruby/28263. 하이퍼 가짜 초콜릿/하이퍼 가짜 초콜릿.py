# 28263 하이퍼 가짜 초콜릿

from random import shuffle
from functools import reduce

L = 6659452800
P = [
    10672201,
    12806641,
    13759201,
    14229601,
    14414401,
    15135121,
    15855841,
    16648633,
    16816801,
    17075521,
    19027009,
    19819801,
    20180161,
    23783761,
    24216193,
    24393601,
    25225201,
    27747721,
    28828801,
    30830801,
    32016601,
    43243201,
    44396353,
    45302401,
    46246201,
    51226561,
    52852801,
    55495441,
    60540481,
    63423361,
    66594529,
    67953601,
    69369301,
    79279201,
    85377601,
    95135041,
]

mod_set_dict1 = {}
mod_set_dict2 = {}
while True:
    shuffle(P)
    set1 = set(P[:5])
    set2 = set(P[5:11])
    set1_value = reduce(lambda x, y: x * y, set1) % L
    set2_value = reduce(lambda x, y: x * y, set2) % L
    set1_inverse = pow(set1_value, -1, L)
    set2_inverse = pow(set2_value, -1, L)
    mod_set_dict1[set1_value] = set1
    mod_set_dict2[set2_value] = set2
    if set1_inverse in mod_set_dict2 and mod_set_dict2[set1_inverse].isdisjoint(set1):
        result = list(set1.union(mod_set_dict2[set1_inverse]))
        result.sort()
        print(*result)
        break
    if set2_inverse in mod_set_dict1 and mod_set_dict1[set2_inverse].isdisjoint(set2):
        result = list(set2.union(mod_set_dict1[set2_inverse]))
        result.sort()
        print(*result)
        break
