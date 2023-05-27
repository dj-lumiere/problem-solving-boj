# 1437 수 분해

N = int(input())
result_for_smaller_values = [0, 1, 2, 3]
MOD = 10_007
if N <= 3:
    print(result_for_smaller_values[N])
else:
    # x**(N/x)가 e에서 최대가 되므로, 3을 최대한 많이 가져가게 만들기
    maximum_three_count, residue = divmod(N, 3)
    if residue == 0:
        print(pow(3, maximum_three_count, MOD))
    elif residue == 1:
        print(pow(3, maximum_three_count - 1, MOD) * 4 % MOD)
    elif residue == 2:
        print(pow(3, maximum_three_count, MOD) * 2 % MOD)