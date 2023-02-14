N, M = list(map(int, input().split(" ")))
nCm_denom = 1
nCm_nom = 1
for i in range(1, N+1):
    nCm_denom *= i
    if i <= M:
        nCm_nom *= i
    else:
        nCm_nom *= i-M
print(nCm_denom // nCm_nom)