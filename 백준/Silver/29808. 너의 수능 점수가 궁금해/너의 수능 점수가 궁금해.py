# 29808 너의 수능 점수가 궁금해

from itertools import product


def make_id_number(kor_eng_diff, math_sci_diff):
    number = 0
    if kor_eng_diff > 0:
        number += (kor_eng_diff) * 508
    else:
        number += (-kor_eng_diff) * 108
    if math_sci_diff > 0:
        number += (math_sci_diff) * 212
    else:
        number += (-math_sci_diff) * 305
    return number * 4763


possible_scores = []
number = int(input())
for kor_eng_diff, math_sci_diff in product(range(-200, 201), repeat=2):
    if make_id_number(kor_eng_diff, math_sci_diff) == number:
        possible_scores.append((abs(kor_eng_diff), abs(math_sci_diff)))
possible_scores.sort(key=lambda x: (x[0], x[1]))
print(len(possible_scores))
for i in possible_scores:
    print(*i)