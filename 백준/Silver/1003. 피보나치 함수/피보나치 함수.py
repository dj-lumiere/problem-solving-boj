from sys import stdin, stdout

test_case = int(input())

def loading_list_n(n: int) -> list:
    string_list = []
    while n:
        n -= 1
        string_element = stdin.readline().rstrip()
        string_list.append(int(string_element))
    return string_list

fibonacci_test_list = loading_list_n(test_case)

def count_call0(n: int) -> int:
    memo = [0,0]
    for i in range(n+1):
        if i == 0:
            memo[i%2] = 1
        elif i == 1:
            memo[i%2] = 0
        else:
            memo[i%2] = memo[0] + memo[1]
    return(memo[n%2])

def count_call1(n: int) -> int:
    memo = [0,0]
    for i in range(n+1):
        if i == 0:
            memo[i%2] = 0
        elif i == 1:
            memo[i%2] = 1
        else:
            memo[i%2] = memo[0] + memo[1]
    return(memo[n%2])

for i in fibonacci_test_list:
    stdout.writelines(f"{count_call0(i)} {count_call1(i)}\n")