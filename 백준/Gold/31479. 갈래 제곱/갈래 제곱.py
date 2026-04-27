# 31497 갈래 제곱

from fractions import Fraction
from re import split


def parse_formula(formula: str) -> list[Fraction]:
    formula = "+" + formula if formula[0] in ["x", "C"] else formula
    x_powers = [f"x^{i}" for i in range(500, 1, -1)] + ["x"]
    coefficients_str = split("(" + r"|".join(x_powers).replace("^", r"\^") + ")", formula)
    coefficients_str = [i for i in coefficients_str if i]
    # print(coefficients_str)
    coefficients = [Fraction(0) for _ in range(501)]
    for i, v in enumerate(coefficients_str):
        if v == "+":
            coefficients_str[i] = "+1"
        if v == "-":
            coefficients_str[i] = "-1"
        if v == "x":
            coefficients_str[i] = v = "x^1"
        if v[:2] == "x^":
            coefficients[int(v[2:])] = Fraction(coefficients_str[i - 1]) if coefficients_str[i - 1] != "+C" else Fraction(0)
    if coefficients_str[-1] != "+D" and coefficients_str[-1][:2] != "x^":
        coefficients[0] = Fraction(coefficients_str[-1])
    # print(coefficients)
    return coefficients


def sol(coefficients1: list[Fraction], coefficients2: list[Fraction]) -> bool:
    coefficients1.extend([Fraction(0)] * 2)
    return all(coefficients1[i] * i * (i - 1) == coefficients2[i - 2] for i in range(2, len(coefficients1)))


T = int(input())
for _ in range(T):
    formula1, formula2 = input().split()
    print("Yes" if sol(parse_formula(formula1), parse_formula(formula2)) else "No")
