t = int(input())
for _ in range(t):
    l, r, s = map(int, input().split())
    left_side_step = (s - l) * 2 + 1
    right_side_step = (r - s) * 2
    print(min(left_side_step, right_side_step))
