# 25192 인사성 밝은 곰곰이
from sys import stdin

input = stdin.readline
n = int(input())
person_list = []
answer = 0
answer_sub = 0
for i in range(n):
    name = input().strip()
    if name == "ENTER":
        person_list = list(set(person_list))
        answer_sub = len(person_list)
        answer += answer_sub
        person_list.clear()
        continue
    person_list.append(name)
person_list = list(set(person_list))
answer_sub = len(person_list)
answer += answer_sub
person_list.clear()
print(answer)