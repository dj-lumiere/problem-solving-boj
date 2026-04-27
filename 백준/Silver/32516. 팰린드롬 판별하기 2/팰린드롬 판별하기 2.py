n = int(input())
s = list(input())
answer = 0
for i in range(n//2):
    if s[i] != "?" and s[-i-1] != "?" and s[i] != s[-i-1]:
        answer = 0
        break
    if s[i] == "?" and s[-i-1] == "?":
        answer += 26
    elif s[i] == "?" or s[-i-1] == "?":
        answer += 1
print(answer)