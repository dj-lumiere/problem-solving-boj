import os

tokens = iter(os.read(0, os.fstat(0).st_size).split())
t = int(next(tokens))
answers = ["" for _ in range(t)]
for i in range(t):
    value, unit = float(next(tokens)), next(tokens).decode()
    if unit == "kg":
        value *= 2.2046
        unit = "lb"
    elif unit == "lb":
        value *= 0.4536
        unit = "kg"
    elif unit == "l":
        value *= 0.2642
        unit = "g"
    elif unit == "g":
        value *= 3.7854
        unit = "l"
    print(f"{value:.4f} {unit}")