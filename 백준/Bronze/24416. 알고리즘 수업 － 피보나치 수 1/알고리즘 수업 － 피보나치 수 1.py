# 24416 알고리즘 수업 - 피보나치 수 1

n: int = int(input())
fib_list: list[int] = []
for i in range(40 + 1):
    if i == 0:
        fib_list.append(0)
    elif i == 1:
        fib_list.append(1)
    else:
        fib_list.append(fib_list[-1]+fib_list[-2])
print(f"{fib_list[n]} {n-2}")