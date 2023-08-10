# 27466 그래서 대회 이름 뭐로 하죠

N, M = map(int, input().split(" "))
S = input()
has_good_name = [False, False, False, False]
last_vowel_index = 0
last_consonant_index = 0
VOWELS = ["A", "E", "I", "O", "U"]
for i, v in enumerate(reversed(S)):
    if not has_good_name[0] and v not in VOWELS:
        has_good_name[0] = True
        last_consonant_index = -i - 1
        continue
    if has_good_name[0] and not has_good_name[1] and v == "A":
        has_good_name[1] = True
        continue
    if has_good_name[0] and has_good_name[1] and v == "A":
        has_good_name[2] = True
        last_vowel_index = -i - 1
        break
if N + (last_vowel_index) >= M - 3:
    has_good_name[3] = True
if all(has_good_name):
    print("YES")
    print(S[: M - 3], "AA", S[last_consonant_index], sep="")
else:
    print("NO")