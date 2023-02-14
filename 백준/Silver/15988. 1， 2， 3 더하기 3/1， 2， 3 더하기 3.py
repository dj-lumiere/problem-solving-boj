# 15988 1, 2, 3 더하기 3

memo = [0, 1, 1]  # f(-1), f(0), f(1)임에 주의!!!
f_seq = [0, 1]
mod = 1000000009
for i in range(2, 1000000 + 1):
    memo[(i + 1) % 3] = sum(memo) % mod
    f_seq.append(memo[(i + 1) % 3])
test_case = int(input())
for _ in range(test_case):
    print(f_seq[int(input())])