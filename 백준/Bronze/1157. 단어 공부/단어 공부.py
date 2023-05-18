# 1157 단어 공부

from collections import Counter

string_counter: Counter[str] = Counter(list(input().upper()))
string_counter_sorted: list[tuple] = sorted(string_counter.items(), key=lambda x: -x[1])

max_letter_count: int = 0
max_letter: str = ""

for i, j in string_counter_sorted:
    if j > max_letter_count:
        max_letter_count = j
        max_letter = i
    elif j == max_letter_count:
        max_letter = "?"
        break
print(max_letter)