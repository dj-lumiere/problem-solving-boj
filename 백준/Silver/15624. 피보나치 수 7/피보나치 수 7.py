# 15624 피보나치 수 7

fib_list: list[int] = [0, 1, 1]
for i in range(3, 1000000 + 1):
    fib_list.append(sum(fib_list[-2:]) % 1_000_000_007)
print(fib_list[int(input())])