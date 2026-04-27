q = int(input())
for _ in range(q):
    s = input()
    print(sum("".join(v) == "WOW" for v in zip(s, s[1:], s[2:])))