# 29812 아니 이게 왜 안 돼

from collections import Counter


N = int(input())
S = list(input())
letter_frequency = Counter(S)
D, M = map(int, input().split(" "))

other_letter_cluster_length = []
for letter in S:
    if letter in ("H", "Y", "U") and (
        not other_letter_cluster_length or other_letter_cluster_length[-1] != 0
    ):
        other_letter_cluster_length.append(0)
        continue
    if letter in ("H", "Y", "U"):
        continue
    if letter not in ("H", "Y", "U") and not other_letter_cluster_length:
        other_letter_cluster_length.append(1)
        continue
    if letter not in ("H", "Y", "U") and other_letter_cluster_length:
        other_letter_cluster_length[-1] += 1
        continue
if other_letter_cluster_length and other_letter_cluster_length[-1] == 0:
    other_letter_cluster_length.pop()

min_energy = 0
for length in other_letter_cluster_length:
    min_energy += min(D + M, D * length)

hyu_max_count = min(
    letter_frequency.get("H", 0),
    letter_frequency.get("Y", 0),
    letter_frequency.get("U", 0),
)

answer = ["", ""]
if min_energy == 0:
    answer[0] = "Nalmeok"
else:
    answer[0] = min_energy
if hyu_max_count == 0:
    answer[1] = "I love HanYang University"
else:
    answer[1] = hyu_max_count
print(*answer, sep="\n")