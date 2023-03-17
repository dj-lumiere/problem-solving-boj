# 27231 2023년이 기대되는 이유

from math import log2

def permut(N:int, M:int) -> list[list[int]]:
    list_permut = []
    stack = []
    def dfs(init, M, stack):
        if M == 0:
            list_permut.append(stack[:])
            return
        else:
            #중복순열
            for i in range(1, N+1):
                stack.append(i)
                dfs(i, M-1, stack)
                stack.pop()
    dfs(1, M, stack)

    return list_permut

test_case = int(input())
for i in range(test_case):
    # 1과 0으로만 되어있으면 갯수가 무한함
    n = input()
    n_list = [int(i) for i in n]
    if max(n_list) == 1:
        print("Hello, BOJ 2023!")
    elif len(n) == 1:
        print(1)
    else:
        list_permut = permut(2, len(n) - 1)
        number_list_permutated:list[list[int]] = []
        for k in list_permut:
            # 1이면 사이에 +가 들어간걸로 취급, 2면 숫자를 잇기
            number_list:list[str] = [str(n_list[0])]
            for i,j in enumerate(k):
                if j == 2:
                    number_list[-1] = number_list[-1]+str(n_list[i+1])
                else:
                    number_list.append(str(n_list[i+1]))
            first_digit_zero_check = False
            for i in number_list:
                if i[0] == "0" and len(i) != 1:
                    first_digit_zero_check = True
                    break
            if not first_digit_zero_check:
                number_list_permutated.append(list(map(int, number_list)))
        # 더하기 위치를 아무데서나 할 수 있게 구현해야함
        m_availability_check = [False for i in range(11+1)]
        for number_list_permutated_element in number_list_permutated:
            for j in range(1, 11+1):
                if sum(number_list_permutated_element) == sum([n**j for n in n_list]) and not m_availability_check[j]:
                    m_availability_check[j] = True
        print(sum(m_availability_check))