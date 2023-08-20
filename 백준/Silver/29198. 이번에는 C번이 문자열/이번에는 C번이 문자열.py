# C번 - 이번에는 C번이 문자열

# Subtask 1
N, M, K = map(int, input().split(" "))
words = []
for _ in range(N):
    word = input()
    words.append(word)
words.sort()
print(*words[:K], sep="")