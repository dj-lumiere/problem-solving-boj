# 30924 A+B - 10 (제2편)
from random import shuffle

A = [i for i in range(1, 10001)]
B = [i for i in range(1, 10001)]
shuffle(A)
shuffle(B)
a = 0
b = 0
ask_count = 0
while A and ask_count <= 9999:
    i = A.pop()
    print(f"? A {i}", flush=True)
    result = int(input())
    ask_count += 1
    if result:
        a = i
        break
else:
    a = A[-1]
while B and ask_count <= 19997:
    i = B.pop()
    print(f"? B {i}", flush=True)
    result = int(input())
    ask_count += 1
    if result:
        b = i
        break
else:
    b = B[-1]
print(f"! {a+b}")