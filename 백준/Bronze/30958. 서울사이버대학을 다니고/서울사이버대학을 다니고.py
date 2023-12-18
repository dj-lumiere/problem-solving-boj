# 30958 서울사이버대학을 다니고

from collections import Counter
from string import ascii_lowercase

_, S = input(), input()
print(max(Counter([i for i in S if i in ascii_lowercase]).values()))