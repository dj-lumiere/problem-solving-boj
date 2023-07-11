# B번 - 2023 아주머학교 프로그래딩 정시머힌

from sys import stdin, stdout
from re import split

input = stdin.readline
print = stdout.write

substitute_list = {
    "@": "a",
    "[": "c",
    "!": "i",
    ";": "j",
    "^": "n",
    "0": "o",
    "7": "t",
    "\\'": "v",
    "\\\\'": "w",
}

N = int(input())
for _ in range(N):
    raw_string = input().strip()
    letter_list = split(r"(@|\[|!|;|\^|0|7|\\\\\'|\\\'|[a-z])", raw_string)
    letter_list_without_blank = [i for i in letter_list if len(i)]
    substitution_count = 0
    for index, letter in enumerate(letter_list_without_blank):
        if letter in substitute_list:
            letter_list_without_blank[index] = substitute_list[letter]
            substitution_count += 1
    after_substitution_result = "".join(letter_list_without_blank)
    if substitution_count >= len(after_substitution_result) / 2:
        print("I don't understand\n")
    else:
        print(f"{after_substitution_result}\n")