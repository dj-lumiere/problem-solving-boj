# 2941 크로아티아 알파벳

import re

test_string = input()
test_word = re.split(r"(c=|c-|dz=|d-|lj|nj|s=|z=|[a-z])", test_string)
result = 0
for letter in test_word:
    if letter:
        result += 1
print(result)