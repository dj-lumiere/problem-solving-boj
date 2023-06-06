# 1110 더하기 사이클

N = int(input())
counter = 1
next_N = N
while True:
    n_list = list(str(next_N))
    next_N = int(n_list[-1])*10+(sum(map(int, n_list))%10)
    if next_N != N:
        counter += 1
    else:
        print(counter)
        break