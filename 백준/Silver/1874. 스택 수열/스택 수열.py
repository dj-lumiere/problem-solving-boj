from sys import stdin
N = int(input())
num_list = [int(stdin.readline().rstrip()) for i in range(N)]
visited = [0 for i in range(0,N+1)]
operation_list = []
stack_counter = 0
try:
    for i in num_list:
        if stack_counter < i:
            for j in range(stack_counter+1, i+1):
                stack_counter += 1
                if visited[j] == 2 and j == i:
                    raise ValueError
                elif not visited[j]:
                    visited[j] += 1
                    operation_list.append("+")
        if stack_counter >= i:
            for j in range(stack_counter, i - 1, -1):
                stack_counter -= 1
                if visited[j] == 1:
                    visited[j] += 1
                    operation_list.append("-")
                elif visited[j] == 2 and j == i:
                    raise ValueError
    print("\n".join(operation_list))
except:
    print("NO")