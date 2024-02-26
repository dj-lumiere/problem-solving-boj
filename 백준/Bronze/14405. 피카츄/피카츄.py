# 14405 피카츄

import re

s = input()
s_split = re.split("pi|ka|chu", s)
print("YES" if all(not i for i in s_split) else "NO")