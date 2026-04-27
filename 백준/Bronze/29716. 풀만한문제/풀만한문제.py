# 29716 풀만한문제


def letter_size(letter):
    if ord("A") <= ord(letter) <= ord("Z"):
        return 4
    if ord("a") <= ord(letter) <= ord("z"):
        return 2
    if ord("0") <= ord(letter) <= ord("9"):
        return 2
    return 1


j, n = map(int, input().split(" "))
answer = 0
for _ in range(n):
    word_sum = sum(map(letter_size, list(input())))
    if word_sum <= j:
        answer += 1
print(answer)
