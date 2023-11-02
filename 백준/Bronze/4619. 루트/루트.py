# 4619 루트

while True:
    B, N = map(int, input().split(" "))
    if B == N == 0:
        break
    A1 = int(B ** (1 / N))
    A2 = A1 + 1
    if abs(A1**N - B) >= abs(A2**N - B):
        print(A2)
    else:
        print(A1)