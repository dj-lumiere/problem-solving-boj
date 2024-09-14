from math import atan, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt


def P6(n):
    # ADD ADDITIONAL CODE HERE!
    if n == 1:
        return 3
    return int(pi / atan(1 / sqrt(n)))