# 1541 잃어버린 괄호
import re

formula = input()
formula_splitted = re.split(r"(\+|\-)", formula)
numbers_in_formula = []
is_negative = False
for i, v in enumerate(formula_splitted):
    if not v:
        continue
    elif v == "+":
        is_negative = False
    elif v == "-":
        is_negative = True
    elif v.isdigit() and not is_negative:
        numbers_in_formula.append(int(v))
    elif v.isdigit() and is_negative:
        numbers_in_formula.append(-int(v))
is_negative = False
for i, v in enumerate(numbers_in_formula):
    if v < 0 and not is_negative:
        is_negative = True
    elif v > 0 and is_negative:
        numbers_in_formula[i] = -v
print(sum(numbers_in_formula))
