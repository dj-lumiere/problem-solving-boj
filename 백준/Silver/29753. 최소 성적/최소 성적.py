# 29753 최소 성적

from decimal import Decimal

N, X = map(Decimal, input().strip().split(" "))
N = int(N)
total_score = Decimal(0)
total_class_count = Decimal(0)
class_score_dict = {
    "A+": Decimal("4.50"),
    "A0": Decimal("4.00"),
    "B+": Decimal("3.50"),
    "B0": Decimal("3.00"),
    "C+": Decimal("2.50"),
    "C0": Decimal("2.00"),
    "D+": Decimal("1.50"),
    "D0": Decimal("1.00"),
    "F": Decimal("0"),
}
score_class_dict = {v: i for i, v in class_score_dict.items()}
for _ in range(N - 1):
    class_count, score = input().strip().split(" ")
    class_count = Decimal(class_count)
    total_class_count += class_count
    total_score += class_count * class_score_dict[score]
last_class_count = int(input())
total_class_count += last_class_count
result = ""
for i, v in reversed(class_score_dict.items()):
    if (
        Decimal(
            int(Decimal((total_score + last_class_count * v) / total_class_count) * 100)
        )
        / Decimal(100)
        > X
    ):
        print(i)
        break
    result = i
else:
    print("impossible")