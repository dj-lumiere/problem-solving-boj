from sys import setrecursionlimit

setrecursionlimit(10**5)

N = input()
N_len = len(N)
N_list = [int(N[i]) for i in range(N_len)]
memo = dict()
def count(N_list) -> int:
    if N_list[0] == 0:
        memo[tuple(N_list)] = 0
    else:
        if len(N_list) == 1:
            memo[tuple(N_list)] = 1
        elif len(N_list) == 2:
            if N_list[1] == 0 and N_list[0] >= 3:
                memo[tuple(N_list)] = 0
            elif 10 <= N_list[0] * 10 + N_list[1] <= 26 and N_list[1] != 0:
                memo[tuple(N_list)] = 2
            else:
                memo[tuple(N_list)] = 1
        else:
            first_digit = N_list[0]
            second_digit = N_list[1]
            if tuple(N_list[1:]) not in memo:
                memo[tuple(N_list[1:])] = count(N_list[1:])
            if tuple(N_list[2:]) not in memo:
                memo[tuple(N_list[2:])] = count(N_list[2:])
            if first_digit * 10 + second_digit <= 26:
                if second_digit:
                    memo[tuple(N_list)] = (memo[tuple(N_list[1:])]+memo[tuple(N_list[2:])]) % 1000000
                else:
                    memo[tuple(N_list)] = memo[tuple(N_list[2:])]
            else:
                memo[tuple(N_list)] = memo[tuple(N_list[1:])]
    return memo[tuple(N_list)]
print(count(N_list))