# 26151 NATO 음성 기호와 쿼리

from bisect import bisect_right
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


THRESHOLD = 27
x = [[1] * 26] + [[0] * 26 for _ in range(THRESHOLD)]
NATO = (
    "ALFA",
    "BRAVO",
    "CHARLIE",
    "DELTA",
    "ECHO",
    "FOXTROT",
    "GOLF",
    "HOTEL",
    "INDIA",
    "JULIETT",
    "KILO",
    "LIMA",
    "MIKE",
    "NOVEMBER",
    "OSCAR",
    "PAPA",
    "QUEBEC",
    "ROMEO",
    "SIERRA",
    "TANGO",
    "UNIFORM",
    "VICTOR",
    "WHISKEY",
    "XRAY",
    "YANKEE",
    "ZULU",
)
for i in range(1, THRESHOLD + 1):
    for j in range(26):
        for k in NATO[j]:
            x[i][j] += x[i - 1][ord(k) - ord("A")]
# for i in x:
#     print(" ".join(map(str, i)))
S, Q = input().split(" ")
Q = int(Q)
step = 0
threshold_level = THRESHOLD + 1
# print(threshold_level)
INF = 2*10**18
precalculation = [[0] * (len(S) + 1) for _ in range(threshold_level)]
for i in range(threshold_level):
    for j, letter in enumerate(S, start=1):
        letter_order = ord(letter) - ord("A")
        precalculation[i][j] = min(precalculation[i][j - 1] + x[i][letter_order], INF)
# print(*precalculation, sep="\n")
answer = ""
for _ in range(Q):
    operator, operand = map(int, input().split(" "))
    # print(operator, operand)
    if operator == 1:
        step += operand
    if operator == 2:
        stack = []
        operand -= 1
        if step >= threshold_level-1:
            stack.append((operand, ord(S[0]) - ord("A"), threshold_level-1))
        else:
            stack.append((operand, -1, step))
        while stack:
            length, last_letter, stage = stack.pop()
            #print(length, last_letter, stage)
            if stage == -1:
                print(chr(ord("A") + last_letter), end="")
                continue
            letter_length = [0]
            if last_letter == -1:
                letter_length = precalculation[stage]
            else:
                for letter in NATO[last_letter]:
                    letter_length.append(
                        letter_length[-1] + x[stage][ord(letter) - ord("A")]
                    )
            #print(letter_length)
            index = bisect_right(letter_length, length)
            #print(index)
            current_letter = 0
            if last_letter == -1:
                current_letter = ord(S[index - 1]) - ord("A")
            else:
                current_letter = ord(NATO[last_letter][index - 1]) - ord("A")
            stack.append((length - letter_length[index - 1], current_letter, stage - 1))
