# 17214 다항 함수의 적분

f_x = input()
if f_x[-1] == "x":
    A, B = int(f_x[:-1]), 0
elif "x" not in f_x:
    A, B = 0, int(f_x)
else:
    A, B = list(map(int, f_x.split("x")))
new_A = A // 2
new_B = B

if new_A == 1:
    print("xx", end="")
elif new_A == -1:
    print("-xx", end="")
elif new_A == 0:
    print("", end="")
else:
    print(f"{new_A}xx", end="")

if new_B == 1 and new_A != 0:
    print("+x", end="")
elif new_B == 1 and new_A == 0:
    print("x", end="")
elif new_B == -1:
    print("-x", end="")
elif new_B == 0:
    print("", end="")
elif new_B > 0 and new_A != 0:
    print(f"+{new_B}x", end="")
else:
    print(f"{new_B}x", end="")

if new_A == 0 and new_B == 0:
    print("W")
else:
    print("+W")