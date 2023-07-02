# 1159 농구 경기

n = int(input())
family_name_initial_frequency = [0] * 26
result = ""
for _ in range(n):
    family_name = input()
    family_name_initial = family_name[0]
    family_name_initial_frequency[ord(family_name_initial) - ord("a")] += 1
for index, value in enumerate(family_name_initial_frequency):
    if value >= 5:
        result += chr(ord("a") + index)
if not result:
    print("PREDAJA")
else:
    print(result)