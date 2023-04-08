# 2417 정수 제곱근

N = list(map(int, input()))
if len(N) % 2:
    N = [N[0]] + [10 * N[2 * i + 1] + N[2 * i + 2] for i in range(len(N) // 2)]
else:
    N = [10 * N[2 * i + 0] + N[2 * i + 1] for i in range(len(N) // 2)]
# 개평법 세팅
remainder = 0
divisor = 0
answer = 0
for i, j in enumerate(N):
    remainder = 100 * remainder + j
    for k in range(1, 10 + 1):
        if (divisor * 10 + k) * k > remainder:
            divisor = divisor * 10 + (k - 1)
            remainder -= divisor * (k - 1)
            answer = answer * 10 + (k - 1)
            divisor += k - 1
            break
print(answer + 1 if remainder else answer)