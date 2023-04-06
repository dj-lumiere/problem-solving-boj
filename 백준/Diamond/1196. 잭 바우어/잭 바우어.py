# 1196 잭 바우어

from decimal import Decimal, getcontext

getcontext().prec = 400

e = Decimal(
    "2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274"
)
gamma = Decimal(
    "0.57721566490153286060651209008240243104215933593992359880576723488486772677766467093694706329174674951463144724980708248096050401448654283622417399764492353625350033374293733773767394279259525824709491600873520394816567085323315177661152862119950150798479374"
)

# 조화수열의 합

N, K = list(map(Decimal, input().split(" ")))
approximation = (
    lambda N: Decimal(N).log10() / Decimal(e).log10()
    + gamma
    + Decimal(1) / Decimal(2 * N)
    - Decimal(1) / Decimal(12 * N**2)

)
answer: Decimal = Decimal(0)
answer2: Decimal = Decimal(0)
if N <= 300:
    for i in range(1, int(N + 1)):
        answer += 1 / Decimal(i)
else:
    answer = approximation(N)
if N - K < 1:
    answer2 = Decimal(0)
elif N - K <= 300:
    for i in range(1, int(N - K + 1)):
        answer2 += 1 / Decimal(i)
else:
    answer2 = approximation(N - K)
print(N*(answer-answer2))