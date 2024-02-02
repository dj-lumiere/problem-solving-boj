# 4458 첫 글자를 대문자로


def initial_letter_upper(word: str):
    return word[0].upper() + word[1:]


N = int(input())
for _ in range(N):
    print(initial_letter_upper(input()))
