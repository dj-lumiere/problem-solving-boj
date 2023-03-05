# 16139 인간-컴퓨터 상호작용

string = list(input())
letter_count = [[0] for _ in range(26)]
for (i, j) in enumerate(string):
    letter_value = ord(j) - ord("a")
    for k in range(26):
        if k == letter_value:
            letter_count[k].append(letter_count[k][-1] + 1)
        else:
            letter_count[k].append(letter_count[k][-1])
n = int(input())
for _ in range(n):
    a, l, r = list(map(str, input().split(" ")))
    letter_number = ord(a) - ord("a")
    right_int = int(r) + 1
    left_int = int(l)
    print(
        letter_count[letter_number][right_int] - letter_count[letter_number][left_int]
    )