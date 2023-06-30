# 1032 명령 프롬프트

n = int(input())
commands = [input() for _ in range(n)]
answer = ""
for letters in zip(*commands):
    if all([i == letters[0] for i in letters]):
        answer += letters[0]
    else:
        answer += "?"
print(answer)