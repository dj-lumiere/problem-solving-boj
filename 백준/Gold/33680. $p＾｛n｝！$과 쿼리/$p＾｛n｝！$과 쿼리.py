q = int(input())
MOD = 10**9+7
answers = []
for _ in range(q):
    p, n = map(int, input().split())
    answer = (pow(p, n, MOD) - 1) * pow(p-1, -1, MOD) % MOD
    answers.append(answer)
print("\n".join(map(str, answers)))