# 2448 별 찍기

from math import log2

N = int(log2(int(input())//3))
base_star = [
    [" ", " ", "*", " ", " "],
    [" ", "*", " ", "*", " "],
    ["*", "*", "*", "*", "*"],
]
x_offset_size = [5]
y_offset_size = [3]
i = 0
while i < N:
    x_offset_size.append(x_offset_size[-1] * 2 + 1)
    y_offset_size.append(y_offset_size[-1] * 2)
    i += 1

star_array = [[" " for _ in range(x_offset_size[-1])] for _ in range(y_offset_size[-1])]


def star_draw(N, x_offset, y_offset):
    if N == 0:
        for i in range(3):
            star_array[y_offset + i][x_offset : x_offset + 5] = base_star[i]
    else:
        star_draw(N - 1, x_offset + (x_offset_size[N - 1] + 1) // 2, y_offset)
        star_draw(N - 1, x_offset, y_offset + y_offset_size[N - 1])
        star_draw(
            N - 1, x_offset + x_offset_size[N - 1] + 1, y_offset + y_offset_size[N - 1]
        )


star_draw(N, 0, 0)
for i in star_array:
    if i == N - 1:
        print("".join(i))
    else:
        print("".join(i) + ' ')