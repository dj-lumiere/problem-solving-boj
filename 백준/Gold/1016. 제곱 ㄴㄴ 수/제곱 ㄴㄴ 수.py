# 1016 제곱 ㄴㄴ 수

# max의 최댓값 ** 1/4까지의 소수들에 대해 제곱을 해서 에라토스테네스의 체 활용
# max * 1/2까진 제곱수 쳐내기(이건 step을 계속 늘려가면서 쳐내면 됨)

x_min, x_max = list(map(int, input().split(" ")))
number_count = x_max-x_min+1

def sol(N: int) -> list[bool]:
    prime_list = [False, False]+[True for i in range(2, N+1)]
    for i in range(int(N**(1/2))+1):
        if prime_list[i]:
            prime_list[i:N+1:i] = [True] + [False]*(N//i-1)
    return prime_list

prime_list = sol(int((x_max)**(1/2))+1)

no_square_list = [True for i in range(x_min, x_max+1)]
for i, j in enumerate(prime_list):
    if i >= int(x_max**.5)+1:
        break
    else:
        if j:
            no_square_list[(-1*x_min)%(i**2):number_count:i**2] = [False]*((x_max//(i**2))-((x_min-1)//(i**2)))
print(sum(no_square_list))