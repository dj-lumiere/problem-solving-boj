while True:
    a, b, c = map(int, input().split())
    if a==b==c==0:
        break
    if b*2==a+c:
        print(f"AP {c*2-b}")
    else:
        print(f"GP {c*c//b}")