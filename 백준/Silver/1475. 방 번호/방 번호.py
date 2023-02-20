# 1475 방 번호

from collections import Counter
from math import ceil

N = input()
number_dict = Counter(list(N))
number_dict["6"] = ceil((number_dict["6"]+number_dict["9"])/2)
number_dict["9"] = 0
print(max(number_dict.values()))