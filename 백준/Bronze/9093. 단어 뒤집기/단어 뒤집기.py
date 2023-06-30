# 9093 단어 뒤집기

T = int(input())
for _ in range(T):
    word_list = list(input().split(" "))
    for i, v in enumerate(word_list):
        word_list[i] = v[::-1]
    print(*word_list)