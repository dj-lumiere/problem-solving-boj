# 11478 서로 다른 부분 문자열의 개수

S = input()
subseqence_set = set()
for i in range(len(S)):
    for j in range(len(S) - i):
        subseqence_set.add(S[j : j + i + 1])
print(len(subseqence_set))