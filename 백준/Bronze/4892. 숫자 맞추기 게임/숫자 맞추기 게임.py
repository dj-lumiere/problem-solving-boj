index = 1
while True:
    n0 = int(input())
    if not n0:
        break
    n1 = 3 * n0
    n2 = (n1 + 1) // 2
    n3 = 3 * n2
    n4 = n3 // 9
    print(f"{index}. {'eovdedn'[n1 % 2::2]} {n4}")
    index += 1