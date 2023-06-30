# 1977 완전제곱수

M, N = int(input()), int(input())
square_count = -1
square_sum = 0
square_min = 100001
for i in range(1, 101):
    if M <= i * i <= N:
        square_count += 1
        square_sum += i * i
        square_min = min(square_min, i * i)
if square_count == -1:
    print(-1)
else:
    print(square_sum, square_min, sep="\n")