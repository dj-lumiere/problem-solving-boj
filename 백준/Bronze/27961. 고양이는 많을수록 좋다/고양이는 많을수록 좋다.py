# 27961 고양이는 많을수록 좋다

N = int(input())
if N == 0:
    print(0)
elif N == 1:
    print(1)
elif N & ((1 << (N.bit_length() - 1)) - 1):
    print(N.bit_length() + 1)
else:
    print(N.bit_length())
