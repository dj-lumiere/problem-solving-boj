# 30988  $\sqrt{f}(x)$


def degree5(coefficients):
    y0 = (
        lambda a, b, c, d, e, f: a * f**5
        + b * f**4
        + c * f**3
        + d * f**2
        + e * f
        + f
    )
    y1 = (
        lambda a, b, c, d, e, f: 5 * a * e * f**4
        + 4 * b * e * f**3
        + 3 * c * e * f**2
        + 2 * d * e * f
        + e**2
    )
    y2 = (
        lambda a, b, c, d, e, f: 5 * a * d * f**4
        + 10 * a * e**2 * f**3
        + 4 * b * d * f**3
        + 6 * b * e**2 * f**2
        + 3 * c * d * f**2
        + 3 * c * e**2 * f
        + 2 * d**2 * f
        + d * e**2
        + d * e
    )
    y3 = (
        lambda a, b, c, d, e, f: 5 * a * c * f**4
        + 20 * a * d * e * f**3
        + 10 * a * e**3 * f**2
        + 4 * b * c * f**3
        + 12 * b * d * e * f**2
        + 4 * b * e**3 * f
        + 3 * c**2 * f**2
        + 6 * c * d * e * f
        + 2 * c * d * f
        + c * e**3
        + c * e
        + 2 * d**2 * e
    )
    y4 = (
        lambda a, b, c, d, e, f: 5 * a * b * f**4
        + 20 * a * c * e * f**3
        + 10 * a * d**2 * f**3
        + 30 * a * d * e**2 * f**2
        + 5 * a * e**4 * f
        + 4 * b**2 * f**3
        + 12 * b * c * e * f**2
        + 3 * b * c * f**2
        + 6 * b * d**2 * f**2
        + 12 * b * d * e**2 * f
        + 2 * b * d * f
        + b * e**4
        + b * e
        + 6 * c**2 * e * f
        + 3 * c * d**2 * f
        + 3 * c * d * e**2
        + 2 * c * d * e
        + d**3
    )
    y5 = (
        lambda a, b, c, d, e, f: 5 * a**2 * f**4
        + 20 * a * b * e * f**3
        + 4 * a * b * f**3
        + 20 * a * c * d * f**3
        + 30 * a * c * e**2 * f**2
        + 3 * a * c * f**2
        + 30 * a * d**2 * e * f**2
        + 20 * a * d * e**3 * f
        + 2 * a * d * f
        + a * e**5
        + a * e
        + 12 * b**2 * e * f**2
        + 12 * b * c * d * f**2
        + 12 * b * c * e**2 * f
        + 6 * b * c * e * f
        + 12 * b * d**2 * e * f
        + 4 * b * d * e**3
        + 2 * b * d * e
        + 6 * c**2 * d * f
        + 3 * c**2 * e**2
        + 3 * c * d**2 * e
        + 2 * c * d**2
    )
    y6 = (
        lambda a, b, c, d, e, f: 20 * a**2 * e * f**3
        + 20 * a * b * d * f**3
        + 30 * a * b * e**2 * f**2
        + 12 * a * b * e * f**2
        + 10 * a * c**2 * f**3
        + 60 * a * c * d * e * f**2
        + 20 * a * c * e**3 * f
        + 6 * a * c * e * f
        + 10 * a * d**3 * f**2
        + 30 * a * d**2 * e**2 * f
        + 5 * a * d * e**4
        + 2 * a * d * e
        + 12 * b**2 * d * f**2
        + 12 * b**2 * e**2 * f
        + 6 * b * c**2 * f**2
        + 24 * b * c * d * e * f
        + 6 * b * c * d * f
        + 4 * b * c * e**3
        + 3 * b * c * e**2
        + 4 * b * d**3 * f
        + 6 * b * d**2 * e**2
        + 2 * b * d**2
        + 3 * c**3 * f
        + 6 * c**2 * d * e
        + c**2 * d
        + c * d**3
    )
    y7 = (
        lambda a, b, c, d, e, f: 20 * a**2 * d * f**3
        + 30 * a**2 * e**2 * f**2
        + 20 * a * b * c * f**3
        + 60 * a * b * d * e * f**2
        + 12 * a * b * d * f**2
        + 20 * a * b * e**3 * f
        + 12 * a * b * e**2 * f
        + 30 * a * c**2 * e * f**2
        + 30 * a * c * d**2 * f**2
        + 60 * a * c * d * e**2 * f
        + 6 * a * c * d * f
        + 5 * a * c * e**4
        + 3 * a * c * e**2
        + 20 * a * d**3 * e * f
        + 10 * a * d**2 * e**3
        + 2 * a * d**2
        + 12 * b**2 * c * f**2
        + 24 * b**2 * d * e * f
        + 4 * b**2 * e**3
        + 12 * b * c**2 * e * f
        + 6 * b * c**2 * f
        + 12 * b * c * d**2 * f
        + 12 * b * c * d * e**2
        + 6 * b * c * d * e
        + 2 * b * c * d
        + 4 * b * d**3 * e
        + 3 * c**3 * e
        + 3 * c**2 * d**2
    )
    y8 = (
        lambda a, b, c, d, e, f: 20 * a**2 * c * f**3
        + 60 * a**2 * d * e * f**2
        + 20 * a**2 * e**3 * f
        + 10 * a * b**2 * f**3
        + 60 * a * b * c * e * f**2
        + 12 * a * b * c * f**2
        + 30 * a * b * d**2 * f**2
        + 60 * a * b * d * e**2 * f
        + 24 * a * b * d * e * f
        + 5 * a * b * e**4
        + 4 * a * b * e**3
        + 30 * a * c**2 * d * f**2
        + 30 * a * c**2 * e**2 * f
        + 6 * a * c**2 * f
        + 60 * a * c * d**2 * e * f
        + 20 * a * c * d * e**3
        + 6 * a * c * d * e
        + 2 * a * c * d
        + 5 * a * d**4 * f
        + 10 * a * d**3 * e**2
        + 6 * b**3 * f**2
        + 24 * b**2 * c * e * f
        + 3 * b**2 * c * f
        + 12 * b**2 * d**2 * f
        + 12 * b**2 * d * e**2
        + b**2 * d
        + 12 * b * c**2 * d * f
        + 6 * b * c**2 * e**2
        + 6 * b * c**2 * e
        + 12 * b * c * d**2 * e
        + 3 * b * c * d**2
        + b * d**4
        + 3 * c**3 * d
    )
    y9 = (
        lambda a, b, c, d, e, f: 20 * a**2 * b * f**3
        + 60 * a**2 * c * e * f**2
        + 30 * a**2 * d**2 * f**2
        + 60 * a**2 * d * e**2 * f
        + 5 * a**2 * e**4
        + 30 * a * b**2 * e * f**2
        + 12 * a * b**2 * f**2
        + 60 * a * b * c * d * f**2
        + 60 * a * b * c * e**2 * f
        + 24 * a * b * c * e * f
        + 6 * a * b * c * f
        + 60 * a * b * d**2 * e * f
        + 12 * a * b * d**2 * f
        + 20 * a * b * d * e**3
        + 12 * a * b * d * e**2
        + 2 * a * b * d
        + 10 * a * c**3 * f**2
        + 60 * a * c**2 * d * e * f
        + 10 * a * c**2 * e**3
        + 6 * a * c**2 * e
        + 20 * a * c * d**3 * f
        + 30 * a * c * d**2 * e**2
        + 3 * a * c * d**2
        + 5 * a * d**4 * e
        + 12 * b**3 * e * f
        + 24 * b**2 * c * d * f
        + 12 * b**2 * c * e**2
        + 3 * b**2 * c * e
        + 12 * b**2 * d**2 * e
        + 4 * b * c**3 * f
        + 12 * b * c**2 * d * e
        + 6 * b * c**2 * d
        + 4 * b * c * d**3
        + c**4
    )
    y10 = (
        lambda a, b, c, d, e, f: 10 * a**3 * f**3
        + 60 * a**2 * b * e * f**2
        + 6 * a**2 * b * f**2
        + 60 * a**2 * c * d * f**2
        + 60 * a**2 * c * e**2 * f
        + 3 * a**2 * c * f
        + 60 * a**2 * d**2 * e * f
        + 20 * a**2 * d * e**3
        + a**2 * d
        + 30 * a * b**2 * d * f**2
        + 30 * a * b**2 * e**2 * f
        + 24 * a * b**2 * e * f
        + 30 * a * b * c**2 * f**2
        + 120 * a * b * c * d * e * f
        + 24 * a * b * c * d * f
        + 20 * a * b * c * e**3
        + 12 * a * b * c * e**2
        + 6 * a * b * c * e
        + 20 * a * b * d**3 * f
        + 30 * a * b * d**2 * e**2
        + 12 * a * b * d**2 * e
        + 20 * a * c**3 * e * f
        + 30 * a * c**2 * d**2 * f
        + 30 * a * c**2 * d * e**2
        + 6 * a * c**2 * d
        + 20 * a * c * d**3 * e
        + a * d**5
        + 12 * b**3 * d * f
        + 6 * b**3 * e**2
        + 12 * b**2 * c**2 * f
        + 24 * b**2 * c * d * e
        + 3 * b**2 * c * d
        + 4 * b**2 * d**3
        + 4 * b * c**3 * e
        + 3 * b * c**3
        + 6 * b * c**2 * d**2
    )
    y11 = (
        lambda a, b, c, d, e, f: 30 * a**3 * e * f**2
        + 60 * a**2 * b * d * f**2
        + 60 * a**2 * b * e**2 * f
        + 12 * a**2 * b * e * f
        + 30 * a**2 * c**2 * f**2
        + 120 * a**2 * c * d * e * f
        + 20 * a**2 * c * e**3
        + 3 * a**2 * c * e
        + 20 * a**2 * d**3 * f
        + 30 * a**2 * d**2 * e**2
        + 30 * a * b**2 * c * f**2
        + 60 * a * b**2 * d * e * f
        + 24 * a * b**2 * d * f
        + 10 * a * b**2 * e**3
        + 12 * a * b**2 * e**2
        + 60 * a * b * c**2 * e * f
        + 12 * a * b * c**2 * f
        + 60 * a * b * c * d**2 * f
        + 60 * a * b * c * d * e**2
        + 24 * a * b * c * d * e
        + 6 * a * b * c * d
        + 20 * a * b * d**3 * e
        + 4 * a * b * d**3
        + 20 * a * c**3 * d * f
        + 10 * a * c**3 * e**2
        + 3 * a * c**3
        + 30 * a * c**2 * d**2 * e
        + 5 * a * c * d**4
        + 12 * b**3 * c * f
        + 12 * b**3 * d * e
        + 12 * b**2 * c**2 * e
        + 3 * b**2 * c**2
        + 12 * b**2 * c * d**2
        + 4 * b * c**3 * d
    )
    y12 = (
        lambda a, b, c, d, e, f: 30 * a**3 * d * f**2
        + 30 * a**3 * e**2 * f
        + 60 * a**2 * b * c * f**2
        + 120 * a**2 * b * d * e * f
        + 12 * a**2 * b * d * f
        + 20 * a**2 * b * e**3
        + 6 * a**2 * b * e**2
        + 60 * a**2 * c**2 * e * f
        + 60 * a**2 * c * d**2 * f
        + 60 * a**2 * c * d * e**2
        + 3 * a**2 * c * d
        + 20 * a**2 * d**3 * e
        + 10 * a * b**3 * f**2
        + 60 * a * b**2 * c * e * f
        + 24 * a * b**2 * c * f
        + 30 * a * b**2 * d**2 * f
        + 30 * a * b**2 * d * e**2
        + 24 * a * b**2 * d * e
        + 60 * a * b * c**2 * d * f
        + 30 * a * b * c**2 * e**2
        + 12 * a * b * c**2 * e
        + 6 * a * b * c**2
        + 60 * a * b * c * d**2 * e
        + 12 * a * b * c * d**2
        + 5 * a * b * d**4
        + 5 * a * c**4 * f
        + 20 * a * c**3 * d * e
        + 10 * a * c**2 * d**3
        + 4 * b**4 * f
        + 12 * b**3 * c * e
        + b**3 * c
        + 6 * b**3 * d**2
        + 12 * b**2 * c**2 * d
        + b * c**4
    )
    y13 = (
        lambda a, b, c, d, e, f: 30 * a**3 * c * f**2
        + 60 * a**3 * d * e * f
        + 10 * a**3 * e**3
        + 30 * a**2 * b**2 * f**2
        + 120 * a**2 * b * c * e * f
        + 12 * a**2 * b * c * f
        + 60 * a**2 * b * d**2 * f
        + 60 * a**2 * b * d * e**2
        + 12 * a**2 * b * d * e
        + 60 * a**2 * c**2 * d * f
        + 30 * a**2 * c**2 * e**2
        + 3 * a**2 * c**2
        + 60 * a**2 * c * d**2 * e
        + 5 * a**2 * d**4
        + 20 * a * b**3 * e * f
        + 12 * a * b**3 * f
        + 60 * a * b**2 * c * d * f
        + 30 * a * b**2 * c * e**2
        + 24 * a * b**2 * c * e
        + 3 * a * b**2 * c
        + 30 * a * b**2 * d**2 * e
        + 12 * a * b**2 * d**2
        + 20 * a * b * c**3 * f
        + 60 * a * b * c**2 * d * e
        + 12 * a * b * c**2 * d
        + 20 * a * b * c * d**3
        + 5 * a * c**4 * e
        + 10 * a * c**3 * d**2
        + 4 * b**4 * e
        + 12 * b**3 * c * d
        + 4 * b**2 * c**3
    )
    y14 = (
        lambda a, b, c, d, e, f: 30 * a**3 * b * f**2
        + 60 * a**3 * c * e * f
        + 30 * a**3 * d**2 * f
        + 30 * a**3 * d * e**2
        + 60 * a**2 * b**2 * e * f
        + 12 * a**2 * b**2 * f
        + 120 * a**2 * b * c * d * f
        + 60 * a**2 * b * c * e**2
        + 12 * a**2 * b * c * e
        + 3 * a**2 * b * c
        + 60 * a**2 * b * d**2 * e
        + 6 * a**2 * b * d**2
        + 20 * a**2 * c**3 * f
        + 60 * a**2 * c**2 * d * e
        + 20 * a**2 * c * d**3
        + 20 * a * b**3 * d * f
        + 10 * a * b**3 * e**2
        + 12 * a * b**3 * e
        + 30 * a * b**2 * c**2 * f
        + 60 * a * b**2 * c * d * e
        + 24 * a * b**2 * c * d
        + 10 * a * b**2 * d**3
        + 20 * a * b * c**3 * e
        + 4 * a * b * c**3
        + 30 * a * b * c**2 * d**2
        + 5 * a * c**4 * d
        + 4 * b**4 * d
        + 6 * b**3 * c**2
    )
    y15 = (
        lambda a, b, c, d, e, f: 10 * a**4 * f**2
        + 60 * a**3 * b * e * f
        + 4 * a**3 * b * f
        + 60 * a**3 * c * d * f
        + 30 * a**3 * c * e**2
        + a**3 * c
        + 30 * a**3 * d**2 * e
        + 60 * a**2 * b**2 * d * f
        + 30 * a**2 * b**2 * e**2
        + 12 * a**2 * b**2 * e
        + 60 * a**2 * b * c**2 * f
        + 120 * a**2 * b * c * d * e
        + 12 * a**2 * b * c * d
        + 20 * a**2 * b * d**3
        + 20 * a**2 * c**3 * e
        + 30 * a**2 * c**2 * d**2
        + 20 * a * b**3 * c * f
        + 20 * a * b**3 * d * e
        + 12 * a * b**3 * d
        + 30 * a * b**2 * c**2 * e
        + 12 * a * b**2 * c**2
        + 30 * a * b**2 * c * d**2
        + 20 * a * b * c**3 * d
        + a * c**5
        + 4 * b**4 * c
    )
    y16 = (
        lambda a, b, c, d, e, f: 20 * a**4 * e * f
        + 60 * a**3 * b * d * f
        + 30 * a**3 * b * e**2
        + 4 * a**3 * b * e
        + 30 * a**3 * c**2 * f
        + 60 * a**3 * c * d * e
        + 10 * a**3 * d**3
        + 60 * a**2 * b**2 * c * f
        + 60 * a**2 * b**2 * d * e
        + 12 * a**2 * b**2 * d
        + 60 * a**2 * b * c**2 * e
        + 6 * a**2 * b * c**2
        + 60 * a**2 * b * c * d**2
        + 20 * a**2 * c**3 * d
        + 5 * a * b**4 * f
        + 20 * a * b**3 * c * e
        + 12 * a * b**3 * c
        + 10 * a * b**3 * d**2
        + 30 * a * b**2 * c**2 * d
        + 5 * a * b * c**4
        + b**5
    )
    y17 = (
        lambda a, b, c, d, e, f: 20 * a**4 * d * f
        + 10 * a**4 * e**2
        + 60 * a**3 * b * c * f
        + 60 * a**3 * b * d * e
        + 4 * a**3 * b * d
        + 30 * a**3 * c**2 * e
        + 30 * a**3 * c * d**2
        + 20 * a**2 * b**3 * f
        + 60 * a**2 * b**2 * c * e
        + 12 * a**2 * b**2 * c
        + 30 * a**2 * b**2 * d**2
        + 60 * a**2 * b * c**2 * d
        + 5 * a**2 * c**4
        + 5 * a * b**4 * e
        + 4 * a * b**4
        + 20 * a * b**3 * c * d
        + 10 * a * b**2 * c**3
    )
    y18 = (
        lambda a, b, c, d, e, f: 20 * a**4 * c * f
        + 20 * a**4 * d * e
        + 30 * a**3 * b**2 * f
        + 60 * a**3 * b * c * e
        + 4 * a**3 * b * c
        + 30 * a**3 * b * d**2
        + 30 * a**3 * c**2 * d
        + 20 * a**2 * b**3 * e
        + 6 * a**2 * b**3
        + 60 * a**2 * b**2 * c * d
        + 20 * a**2 * b * c**3
        + 5 * a * b**4 * d
        + 10 * a * b**3 * c**2
    )
    y19 = (
        lambda a, b, c, d, e, f: 20 * a**4 * b * f
        + 20 * a**4 * c * e
        + 10 * a**4 * d**2
        + 30 * a**3 * b**2 * e
        + 4 * a**3 * b**2
        + 60 * a**3 * b * c * d
        + 10 * a**3 * c**3
        + 20 * a**2 * b**3 * d
        + 30 * a**2 * b**2 * c**2
        + 5 * a * b**4 * c
    )
    y20 = (
        lambda a, b, c, d, e, f: 5 * a**5 * f
        + 20 * a**4 * b * e
        + a**4 * b
        + 20 * a**4 * c * d
        + 30 * a**3 * b**2 * d
        + 30 * a**3 * b * c**2
        + 20 * a**2 * b**3 * c
        + a * b**5
    )
    y21 = (
        lambda a, b, c, d, e, f: 5 * a**5 * e
        + 20 * a**4 * b * d
        + 10 * a**4 * c**2
        + 30 * a**3 * b**2 * c
        + 5 * a**2 * b**4
    )
    y22 = (
        lambda a, b, c, d, e, f: 5 * a**5 * d
        + 20 * a**4 * b * c
        + 10 * a**3 * b**3
    )
    y23 = lambda a, b, c, d, e, f: 5 * a**5 * c + 10 * a**4 * b**2
    y24 = lambda a, b, c, d, e, f: 5 * a**5 * b
    y25 = lambda a, b, c, d, e, f: a**6
    a2 = 0
    for i in range(-100, 101):
        if not i:
            continue
        if i**6 == coefficients[25]:
            a2 = i
            break
    if not a2:
        return []
    result = []
    has_contradiction = True
    for a in [a2, -a2]:
        b = coefficients[24] // (5 * a**5)
        c = (coefficients[23] - 10 * a**4 * b**2) // (5 * a**5)
        d = (coefficients[22] - (20 * a**4 * b * c + 10 * a**3 * b**3)) // (
            5 * a**5
        )
        e = (
            coefficients[21]
            - (
                20 * a**4 * b * d
                + 10 * a**4 * c**2
                + 30 * a**3 * b**2 * c
                + 5 * a**2 * b**4
            )
        ) // (5 * a**5)
        f = (
            coefficients[20]
            - (
                20 * a**4 * b * e
                + a**4 * b
                + 20 * a**4 * c * d
                + 30 * a**3 * b**2 * d
                + 30 * a**3 * b * c**2
                + 20 * a**2 * b**3 * c
                + a * b**5
            )
        ) // (5 * a**5)
        for i in range(26):
            if eval(f"coefficients[{i}] != y{i}(a, b, c, d, e, f)"):
                result = []
                break
        else:
            has_contradiction = False
        if not has_contradiction:
            result = [a, b, c, d, e, f]
            break
    return result


def degree4(coefficients):
    y0 = lambda a, b, c, d, e: a * e**4 + b * e**3 + c * e**2 + d * e + e
    y1 = (
        lambda a, b, c, d, e: 4 * a * d * e**3
        + 3 * b * d * e**2
        + 2 * c * d * e
        + d**2
    )
    y2 = (
        lambda a, b, c, d, e: 4 * a * c * e**3
        + 6 * a * d**2 * e**2
        + 3 * b * c * e**2
        + 3 * b * d**2 * e
        + 2 * c**2 * e
        + c * d**2
        + c * d
    )
    y3 = (
        lambda a, b, c, d, e: 4 * a * b * e**3
        + 12 * a * c * d * e**2
        + 4 * a * d**3 * e
        + 3 * b**2 * e**2
        + 6 * b * c * d * e
        + 2 * b * c * e
        + b * d**3
        + b * d
        + 2 * c**2 * d
    )
    y4 = (
        lambda a, b, c, d, e: 4 * a**2 * e**3
        + 12 * a * b * d * e**2
        + 3 * a * b * e**2
        + 6 * a * c**2 * e**2
        + 12 * a * c * d**2 * e
        + 2 * a * c * e
        + a * d**4
        + a * d
        + 6 * b**2 * d * e
        + 3 * b * c**2 * e
        + 3 * b * c * d**2
        + 2 * b * c * d
        + c**3
    )
    y5 = (
        lambda a, b, c, d, e: 12 * a**2 * d * e**2
        + 12 * a * b * c * e**2
        + 12 * a * b * d**2 * e
        + 6 * a * b * d * e
        + 12 * a * c**2 * d * e
        + 4 * a * c * d**3
        + 2 * a * c * d
        + 6 * b**2 * c * e
        + 3 * b**2 * d**2
        + 3 * b * c**2 * d
        + 2 * b * c**2
    )
    y6 = (
        lambda a, b, c, d, e: 12 * a**2 * c * e**2
        + 12 * a**2 * d**2 * e
        + 6 * a * b**2 * e**2
        + 24 * a * b * c * d * e
        + 6 * a * b * c * e
        + 4 * a * b * d**3
        + 3 * a * b * d**2
        + 4 * a * c**3 * e
        + 6 * a * c**2 * d**2
        + 2 * a * c**2
        + 3 * b**3 * e
        + 6 * b**2 * c * d
        + b**2 * c
        + b * c**3
    )
    y7 = (
        lambda a, b, c, d, e: 12 * a**2 * b * e**2
        + 24 * a**2 * c * d * e
        + 4 * a**2 * d**3
        + 12 * a * b**2 * d * e
        + 6 * a * b**2 * e
        + 12 * a * b * c**2 * e
        + 12 * a * b * c * d**2
        + 6 * a * b * c * d
        + 2 * a * b * c
        + 4 * a * c**3 * d
        + 3 * b**3 * d
        + 3 * b**2 * c**2
    )
    y8 = (
        lambda a, b, c, d, e: 6 * a**3 * e**2
        + 24 * a**2 * b * d * e
        + 3 * a**2 * b * e
        + 12 * a**2 * c**2 * e
        + 12 * a**2 * c * d**2
        + a**2 * c
        + 12 * a * b**2 * c * e
        + 6 * a * b**2 * d**2
        + 6 * a * b**2 * d
        + 12 * a * b * c**2 * d
        + 3 * a * b * c**2
        + a * c**4
        + 3 * b**3 * c
    )
    y9 = (
        lambda a, b, c, d, e: 12 * a**3 * d * e
        + 24 * a**2 * b * c * e
        + 12 * a**2 * b * d**2
        + 3 * a**2 * b * d
        + 12 * a**2 * c**2 * d
        + 4 * a * b**3 * e
        + 12 * a * b**2 * c * d
        + 6 * a * b**2 * c
        + 4 * a * b * c**3
        + b**4
    )
    y10 = (
        lambda a, b, c, d, e: 12 * a**3 * c * e
        + 6 * a**3 * d**2
        + 12 * a**2 * b**2 * e
        + 24 * a**2 * b * c * d
        + 3 * a**2 * b * c
        + 4 * a**2 * c**3
        + 4 * a * b**3 * d
        + 3 * a * b**3
        + 6 * a * b**2 * c**2
    )
    y11 = (
        lambda a, b, c, d, e: 12 * a**3 * b * e
        + 12 * a**3 * c * d
        + 12 * a**2 * b**2 * d
        + 3 * a**2 * b**2
        + 12 * a**2 * b * c**2
        + 4 * a * b**3 * c
    )
    y12 = (
        lambda a, b, c, d, e: 4 * a**4 * e
        + 12 * a**3 * b * d
        + a**3 * b
        + 6 * a**3 * c**2
        + 12 * a**2 * b**2 * c
        + a * b**4
    )
    y13 = (
        lambda a, b, c, d, e: 4 * a**4 * d + 12 * a**3 * b * c + 4 * a**2 * b**3
    )
    y14 = lambda a, b, c, d, e: 4 * a**4 * c + 6 * a**3 * b**2
    y15 = lambda a, b, c, d, e: 4 * a**4 * b
    y16 = lambda a, b, c, d, e: a**5
    a = 0
    for i in range(-100, 101):
        if not i:
            continue
        if i**5 == coefficients[16]:
            a = i
            break
    if not a:
        return []
    b = coefficients[15] // (4 * a**4)
    c = (coefficients[14] - 6 * a**3 * b**2) // (4 * a**4)
    d = (coefficients[13] - (12 * a**3 * b * c + 4 * a**2 * b**3)) // (4 * a**4)
    e = (
        coefficients[12]
        - (
            12 * a**3 * b * d
            + a**3 * b
            + 6 * a**3 * c**2
            + 12 * a**2 * b**2 * c
            + a * b**4
        )
    ) // (4 * a**4)
    for i in range(17):
        if eval(f"coefficients[{i}] != y{i}(a, b, c, d, e)"):
            return []
    return [a, b, c, d, e]


def degree3(coefficients):
    y0 = lambda a, b, c, d: a * d**3 + b * d**2 + c * d + d
    y1 = lambda a, b, c, d: 3 * a * c * d**2 + 2 * b * c * d + c**2
    y2 = (
        lambda a, b, c, d: 3 * a * b * d**2
        + 3 * a * c**2 * d
        + 2 * b**2 * d
        + b * c**2
        + b * c
    )
    y3 = (
        lambda a, b, c, d: 3 * a**2 * d**2
        + 6 * a * b * c * d
        + 2 * a * b * d
        + a * c**3
        + a * c
        + 2 * b**2 * c
    )
    y4 = (
        lambda a, b, c, d: 6 * a**2 * c * d
        + 3 * a * b**2 * d
        + 3 * a * b * c**2
        + 2 * a * b * c
        + b**3
    )
    y5 = (
        lambda a, b, c, d: 6 * a**2 * b * d
        + 3 * a**2 * c**2
        + 3 * a * b**2 * c
        + 2 * a * b**2
    )
    y6 = (
        lambda a, b, c, d: 3 * a**3 * d + 6 * a**2 * b * c + a**2 * b + a * b**3
    )
    y7 = lambda a, b, c, d: 3 * a**3 * c + 3 * a**2 * b**2
    y8 = lambda a, b, c, d: 3 * a**3 * b
    y9 = lambda a, b, c, d: a**4
    a2 = 0
    for i in range(-100, 101):
        if not i:
            continue
        if i**4 == coefficients[9]:
            a2 = i
            break
    if not a2:
        return []
    result = []
    has_contradiction = True
    for a in [a2, -a2]:
        b = coefficients[8] // (3 * a**3)
        c = (coefficients[7] - 3 * a**2 * b**2) // (3 * a**3)
        d = (coefficients[6] - (6 * a**2 * b * c + a**2 * b + a * b**3)) // (
            3 * a**3
        )
        for i in range(10):
            if eval(f"coefficients[{i}] != y{i}(a, b, c, d)"):
                result = []
                break
        else:
            has_contradiction = False
        if not has_contradiction:
            result = [a, b, c, d]
            break
    return result


def degree2(coefficients):
    y0 = lambda a, b, c: a * c**2 + b * c + c
    y1 = lambda a, b, c: 2 * a * b * c + b**2
    y2 = lambda a, b, c: 2 * a**2 * c + a * b**2 + a * b
    y3 = lambda a, b, c: 2 * a**2 * b
    y4 = lambda a, b, c: a**3
    a = 0
    for i in range(-100, 101):
        if not i:
            continue
        if i**3 == coefficients[4]:
            a = i
            break
    if not a:
        return []
    b = coefficients[3] // (2 * a**2)
    c = (coefficients[2] - (a * b**2 + a * b)) // (2 * a**2)
    for i in range(5):
        if eval(f"coefficients[{i}] != y{i}(a, b, c)"):
            return []
    return [a, b, c]


def degree1(coefficients):
    y0 = lambda a, b: a * b + b
    y1 = lambda a, b: a**2
    a2 = 0
    for i in range(-100, 101):
        if not i:
            continue
        if i**2 == coefficients[1]:
            a2 = i
    if not a2:
        return []
    result = []
    has_contradiction = True
    for a in [a2, -a2]:
        b = coefficients[0] // (a + 1)
        for i in range(2):
            if eval(f"coefficients[{i}] != y{i}(a, b)"):
                result = []
                break
        else:
            has_contradiction = False
        if not has_contradiction:
            result = [a, b]
            break
    return result


n = int(input())

f = list(map(int, input().split()))
f.reverse()

if n not in [1, 4, 9, 16, 25]:
    print(-1)
else:
    m = int(n**0.5)
    b = []
    if m == 1:
        b = degree1(f)
    if m == 2:
        b = degree2(f)
    if m == 3:
        b = degree3(f)
    if m == 4:
        b = degree4(f)
    if m == 5:
        b = degree5(f)
    if not b:
        print(-1)
    elif any(not (-100 <= i <= 100) for i in b):
        print(-1)
    else:
        print(m)
        print(*b)
