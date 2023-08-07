# B번 - 끝말잇기

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N = int(input())
word_list = ["."]
for _ in range(N):
    word = input().strip()
    word_list.append(word)
word_list.append(".")
question_mark_position = word_list.index("?")
initial_letter = word_list[question_mark_position - 1][-1]
final_letter = word_list[question_mark_position + 1][0]
M = int(input())
result = ""
for _ in range(M):
    word = input().strip()
    if word in word_list:
        continue
    if initial_letter != "." and word[0] != initial_letter:
        continue
    if final_letter != "." and word[-1] != final_letter:
        continue
    result = word
print(f"{result}")