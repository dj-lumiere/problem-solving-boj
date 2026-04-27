n = int(input())
s = input()
answer = []
for i in s:
    if i.islower():
        answer.append(i.upper())
    else:
        answer.append(i.lower())
print(*answer, sep="")