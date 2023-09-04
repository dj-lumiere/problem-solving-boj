# 10990 별 찍기 - 15

N = int(input())
for i in range(N):
    star_line = [""] * (2 * N - 1)
    star_line[: N - i - 1] = [" "] * (N - i - 1)
    star_line[N - i - 1] = "*"
    if i != 0:
        star_line[N - i : N + i - 1] = [" "] * (2 * i - 1)
        star_line[N + i - 1] = "*"
    print(*star_line, sep="")
