t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if b < 3 * a:
        print(3 * a - b)
    elif b > 4 * a:
        needed_a = (b + 3) // 4
        minimum_b_for_needed_a = needed_a * 3
        print(needed_a - a + max(0, minimum_b_for_needed_a - b))
    else:
        print(0)