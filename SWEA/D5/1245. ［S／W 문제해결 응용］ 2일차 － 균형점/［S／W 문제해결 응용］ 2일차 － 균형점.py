from decimal import Decimal


def sign(x):
    if x == 0:
        return 0
    return x / abs(x)

t = int(input())
answers = []
for hh in range(1, t + 1):
    m = 1
    n = int(input())
    position_weight = list(map(Decimal, input().split()))
    position, weight = position_weight[:n], position_weight[n:]
    result = []
    for x1, x2 in zip(position, position[1:]):
        start = x1
        end = x2
        while start + Decimal("1e-12") < end:
            mid = (start + end) / Decimal(2)
            total_force = sum(m * w / (x - mid) ** 2 * sign(mid - x) for x, w in zip(position, weight))
            if total_force >= 0:
                start = mid
            else:
                end = mid
        result.append(f"{start:.10f}")
    answer = " ".join(result)
    answers.append(f"#{hh} {answer}")
print(*answers, sep="\n")
