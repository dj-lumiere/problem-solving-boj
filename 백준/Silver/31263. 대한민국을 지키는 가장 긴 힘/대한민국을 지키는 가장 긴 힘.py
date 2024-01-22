# 31263 대한민국을 지키는 가장 긴 힘

INF = 10 ** 18
N = int(input())
string = input()
is_valid_substring = [[False for _ in range(N)] for _ in range(3)]
for i in range(N):
    if string[i] == "0":
        continue
    if 1 <= int(string[i: i + 1]) <= 641:
        is_valid_substring[0][i] = True
    if i + 2 > N:
        continue
    if 1 <= int(string[i: i + 2]) <= 641:
        is_valid_substring[1][i] = True
    if i + 3 > N:
        continue
    if 1 <= int(string[i: i + 3]) <= 641:
        is_valid_substring[2][i] = True
answer = [INF for _ in range(N)] + [0 for _ in range(3)]
for i in range(N):
    if is_valid_substring[0][i]:
        answer[i] = min(answer[i], answer[i - 1] + 1)
    if i >= 1 and is_valid_substring[1][i - 1]:
        answer[i] = min(answer[i], answer[i - 2] + 1)
    if i >= 2 and is_valid_substring[2][i - 2]:
        answer[i] = min(answer[i], answer[i - 3] + 1)
# print(*is_valid_substring, sep="\n")
# print(answer)
print(answer[N - 1])