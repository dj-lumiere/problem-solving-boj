# 15824 너 봄에는 캡사이신이 맛있단다

# k번째 원소가 최소인 조합 갯수 : 2**(N-k-1), k번째 원소가 최대인 조합 갯수 : 2**k
# 정렬 후 해보기

N = int(input())
scoville_list = sorted([int(i) for i in input().split(" ")])
MOD = 1_000_000_007
answer = 0
for index, value in enumerate(scoville_list):
    value_as_max = value * pow(2, index, MOD)
    value_as_min = value * pow(2, N - index - 1, MOD)
    answer += value_as_max
    answer -= value_as_min
print(answer % MOD)