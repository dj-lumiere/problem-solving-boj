# 30033 Rust Study

N = int(input())
A, B = list(map(int, input().split())), list(map(int, input().split()))
print(sum(a <= b for a, b in zip(A, B)))