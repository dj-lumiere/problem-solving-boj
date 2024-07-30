e, s, m = map(int, input().split())
for i in range(15 * 28 * 19):
    a, b, c = i % 15 + 1, i % 28 + 1, i % 19 + 1
    if a == e and s == b and c == m:
        print(i + 1)
        break
