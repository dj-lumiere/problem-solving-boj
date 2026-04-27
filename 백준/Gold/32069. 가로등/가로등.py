from bisect import bisect_left, bisect_right

l, n, k = map(int, input().split())
a = list(map(int, input().split()))
color_freq_accsum = [0 for _ in range(k + 2)]
distance = sorted([abs(i - j) - 1 for i, j in zip(a, a[1:])])
color_freq_accsum[0] = l + 1
left_side = a[0]
right_side = l - a[-1]
for i in range(k + 1):
    if i == 0:
        color_freq_accsum[i + 1] = color_freq_accsum[i] - len(a)
        continue
    x = len(distance) - bisect_left(distance, 2 * i - 1)
    y = len(distance) - bisect_left(distance, 2 * i)
    color_freq_accsum[i + 1] = color_freq_accsum[i] - x - y - (left_side >= i) - (right_side >= i)
answer = []
for i, (v1, v2) in enumerate(zip(color_freq_accsum, color_freq_accsum[1:])):
    answer.extend([i]*min(v1-v2, k-len(answer)))
print(*answer, sep="\n")