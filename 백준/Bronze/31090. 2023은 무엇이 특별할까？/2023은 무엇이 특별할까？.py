# 31090 2023은 무엇이 특별할까?

T = int(input())
for _ in range(T):
    N = int(input())
    print("Bye" if (N + 1) % (N % 100) else "Good")