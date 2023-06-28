# 2744 대소문자 바꾸기

S = list(input())
for i,v in enumerate(S):
    if v.isupper():
        S[i] = v.lower()
    if v.islower():
        S[i] = v.upper()
print(*S, sep="")