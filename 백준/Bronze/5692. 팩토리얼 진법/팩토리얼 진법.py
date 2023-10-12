# 5692 팩토리얼 진법


def factorialnary_to_decimal(factorialnary_expr: str) -> int:
    each_digit = [1, 2, 6, 24, 120]
    return sum([int(i) * j for i, j in zip(reversed(factorialnary_expr), each_digit)])


while True:
    number = input()
    if number == "0":
        break
    print(factorialnary_to_decimal(number))