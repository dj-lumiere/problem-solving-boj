# A(-a, 0), B(0, b), C(0, c), D(0, -d) (a>=0, b>=0, c>=0, d>=0)
# M((b-a)//2, 0), N(0, (c-d)//2)
# AB^2=(a+b)^2, CD^2=(c+d)^2, AC^2=a^2+c^2, BD^2=b^2+d^2
# X = a^2+b^2+c^2+d^2
# Y = a^2+2ab+b^2+c^2+2cd+d^2
# Y-X = 2ab+2cd
# W = ((b-a)^2+(c-d)^2)//4=(a^2+b^2+c^2+d^2-2ab-2cd)//4=(X-(Y-X))//4=(2X-Y)//4>=0.
import os

tokens = iter(os.read(0, os.fstat(0).st_size).split())
X, Y = int(next(tokens)), int(next(tokens))
print(2024 * (2 * X - Y) // 4 if X <= Y <= 2 * X else -1)