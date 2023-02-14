from sys import stdout

def combine(N:int, M:int) -> list[list[int]]:
    list_combine = []
    stack = []
    def dfs(init, M, stack):
        if M == 0:
            element = []
            for i in stack:
                element.append(num_list[i-1])
            list_combine.append(element)
            return
        else:
            for i in range(init, N+1):
                stack.append(i)
                dfs(i+1, M-1, stack)
                stack.pop()
    dfs(1, M, stack)
    return list_combine

while True:
    input_str = input()
    if input_str == "0":
        break
    else:
        input_list = input_str.split(" ")
        N = int(input_list[0])
        num_list = input_list[1:]
        combine_list = combine(N, 6)
        for i in combine_list:
            stdout.writelines(" ".join(map(str, i))+"\n")
        stdout.writelines("\n")