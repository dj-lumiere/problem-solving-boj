# 9466 텀 프로젝트
# 사이클을 만들지 못하면 바로 컷...


def find_members_in_cycle(member_count, member_pick):
    visited = [0 for _ in range(member_count + 1)]
    is_in_cycle = 0
    stack = []
    for i in range(1, member_count + 1):
        if visited[i]:
            continue
        stack = [i]
        while stack:
            current_node = stack[-1]
            if visited[current_node]:
                visited[current_node] = 2
                stack.pop()
                continue
            visited[current_node] = 1
            next_node = member_pick[current_node]
            if visited[next_node] == 0:
                stack.append(next_node)
            elif visited[next_node] == 1:  # 사이클 형성
                j = stack.index(next_node)
                is_in_cycle += len(stack) - j
    return is_in_cycle


T = int(input())
for _ in range(T):
    member_count = int(input())
    member_pick = [0] + list(map(int, input().split(" ")))
    print(member_count - find_members_in_cycle(member_count, member_pick))