# 30413 양 한 마리... 양 A마리... 양 A제곱마리...

MOD = 10**9 + 7

A, B = map(int, input().split(" "))
if A == 1:
    print(B % MOD)
else:
    print(pow(A, B, MOD * (A - 1)) // (A - 1))