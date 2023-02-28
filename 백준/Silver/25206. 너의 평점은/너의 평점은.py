# 25206 너의 평점은
from decimal import Decimal

grade_list = {
    "A+": Decimal("4.5"),
    "A0": Decimal("4.0"),
    "B+": Decimal("3.5"),
    "B0": Decimal("3.0"),
    "C+": Decimal("2.5"),
    "C0": Decimal("2.0"),
    "D+": Decimal("1.5"),
    "D0": Decimal("1.0"),
    "F": Decimal("0.0"),
}
grade_total = Decimal(0)
class_time_total = Decimal(0)
while True:
    try:
        class_name, class_time, grade = list(map(str, input().split(" ")))
        class_time = Decimal(class_time)
        if grade != "P":
            grade = grade_list[grade]
            grade_total += grade * class_time
            class_time_total += class_time
    except:
        break
print(grade_total / class_time_total)
