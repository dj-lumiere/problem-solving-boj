# 1725 히스토그램

N = int(input())
hist = [int(input()) for _ in range(N)]


def largest_subhistogram(start, end):
    if start == end:
        return hist[start]
    mid = (start + end) // 2
    left = mid
    right = mid
    height = min(hist[left], hist[right])
    area = height * (right - left + 1)
    while left > start or right < end:
        if right < end and (left == start or hist[left - 1] <= hist[right + 1]):
            right += 1
            height = min(height, hist[right])
        else:
            left -= 1
            height = min(height, hist[left])
        area = max(area, height * (right - left + 1))
    return area


def largest_histogram(N):
    divide_conquer_stack = [(0, N - 1)]
    area = 0
    while divide_conquer_stack:
        start, end = divide_conquer_stack.pop()
        mid = (start + end) // 2
        area = max(area, largest_subhistogram(start, end))
        if start == end:
            continue
        divide_conquer_stack.extend([(start, mid), (mid + 1, end)])
    return area


print(largest_histogram(N))