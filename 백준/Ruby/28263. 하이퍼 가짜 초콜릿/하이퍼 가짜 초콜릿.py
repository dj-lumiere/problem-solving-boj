# 28263 하이퍼 가짜 초콜릿

from random import shuffle
from functools import reduce

L = 5396751360
P = [10378369, 10540531, 11243233, 11531521, 11860993, 12579841, 12849409, 14990977, 16061761, 18170881, 18869761, 19768321, 19987969, 21081061, 24530689, 24984961, 25698817, 27675649, 28108081, 29652481, 32123521, 34594561, 37739521, 39975937, 42831361, 44972929, 46126081, 48185281, 49061377, 61326721, 77096449, 81768961, 84324241, 89945857, 99939841]

mod_set_dict1 = {}
mod_set_dict2 = {}
while True:
    shuffle(P)
    set1 = set(P[:5])
    set2 = set(P[5:11])
    set1_value = reduce(lambda x, y: x * y % L, set1)
    set2_value = reduce(lambda x, y: x * y % L, set2)
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
