# 30917 A+B - 10 (제1편)

A = [i for i in range(1, 10)]
B = [i for i in range(1, 10)]
a = 0
b = 0
while A:
    i = A.pop()
    print(f"? A {i}")
    result = int(input())
    if result:
        a = i
        break
while B:
    i = B.pop()
    print(f"? B {i}")
    result = int(input())
    if result:
        b = i
        break
print(f"! {a+b}")