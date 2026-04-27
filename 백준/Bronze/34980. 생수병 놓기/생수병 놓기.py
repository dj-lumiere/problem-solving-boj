n = int(input())
w1 = list(input())
w2 = list(input())
c1 = w1.count("w")
c2 = w2.count("w")
if w1 == w2:
    print("Good")
elif c1 > c2:
    print("Oryang")
elif c1 == c2:
    print("Its fine")
else:
    print("Manners maketh man")