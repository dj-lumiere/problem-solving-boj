# 9734 순환 소수

from fractions import Fraction

while True:
    try:
        A = input().rstrip()
        int_part = ""
        non_cycling_frac_part = ""
        cycling_frac_part = ""
        int_part_check = True
        non_cycling_frac_part_check = False
        cycling_frac_part_check = False
        for i in list(A):
            if i == ".":
                int_part_check = False
                non_cycling_frac_part_check = True
                cycling_frac_part_check = False
            elif i == "(":
                int_part_check = False
                non_cycling_frac_part_check = False
                cycling_frac_part_check = True
            elif i == ")":
                break
            else:
                if (
                    int_part_check
                    and not non_cycling_frac_part_check
                    and not cycling_frac_part_check
                ):
                    int_part += i
                elif (
                    not int_part_check
                    and non_cycling_frac_part_check
                    and not cycling_frac_part_check
                ):
                    non_cycling_frac_part += i
                elif (
                    not int_part_check
                    and not non_cycling_frac_part_check
                    and cycling_frac_part_check
                ):
                    cycling_frac_part += i
        if non_cycling_frac_part and cycling_frac_part:
            result = (
                Fraction(int(int_part))
                + Fraction(int(non_cycling_frac_part), 10 ** len(non_cycling_frac_part))
                + Fraction(
                    int(cycling_frac_part),
                    (10 ** (len(cycling_frac_part)) - 1)
                    * 10 ** (len(non_cycling_frac_part)),
                )
            )
        elif not non_cycling_frac_part and cycling_frac_part:
            result = Fraction(int(int_part)) + Fraction(
                int(cycling_frac_part), 10 ** (len(cycling_frac_part)) - 1
            )
        elif non_cycling_frac_part and not cycling_frac_part:
            result = (
                Fraction(int(int_part))
                + Fraction(int(non_cycling_frac_part), 10 ** len(non_cycling_frac_part))
            )
        else:
            result = Fraction(int(int_part))
        print(f"{A} = {result.numerator} / {result.denominator}")
    except:
        break