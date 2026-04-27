# 29807 학번을 찾아줘!

T = int(input())
scores = list(map(int, input().split(" ")))
scores += [0] * (5 - T)
number = 0
korean, math, english, science, other_lang = scores

if korean > english:
    number += (korean - english) * 508
else:
    number += (english - korean) * 108
if math > science:
    number += (math - science) * 212
else:
    number += (science - math) * 305

number += other_lang * 707
print(number * 4763)