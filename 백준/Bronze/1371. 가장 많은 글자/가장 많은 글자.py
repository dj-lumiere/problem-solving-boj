# 1371 가장 많은 글자

import os
from string import ascii_lowercase

words = iter(os.read(0, os.fstat(0).st_size).split())
letter_freq = {i: 0 for i in ascii_lowercase}
for word in words:
    for letter in word:
        letter_freq[chr(letter)] += 1
print(*sorted(i for i, v in letter_freq.items() if v == max(letter_freq.values())), sep="")