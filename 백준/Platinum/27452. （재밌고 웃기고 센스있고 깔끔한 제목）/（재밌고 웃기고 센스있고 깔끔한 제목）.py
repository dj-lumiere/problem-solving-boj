# 27452 (재밌고 웃기고 센스있고 깔끔한 제목)

s_length = [0, 2, 2]
while True:
    next_s = sum(s_length[-2:]) + 2
    if next_s > 10**18:
        s_length.append(next_s)
        s_length.append(sum(s_length[-2:]) + 2)
        break
    else:
        s_length.append(next_s)


def find_kth_letter(k: int, level: int) -> str:
    if k == 1:
        return "("
    elif k == s_length[level]:
        return ")"
    elif k <= 1 + s_length[level - 2]:
        return find_kth_letter(k - 1, level - 2)
    else:
        return find_kth_letter(k - 1 - s_length[level - 2], level - 1)


N = int(input())
M = len(s_length) - 2
for i in range(N):
    n, k = map(int, input().split(" "))
    if n >= len(s_length):
        level_offset = ((n - M) // 2) * 2
        n, k = n - level_offset, k - level_offset // 2
    if k < 0:
        print("(")
    elif k > s_length[n]:
        print("0")
    else:
        print(find_kth_letter(k, n))