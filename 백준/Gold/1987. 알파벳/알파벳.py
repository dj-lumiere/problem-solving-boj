# 1987 알파벳
R, C = list(map(int, input().split(" ")))
graph: list[list[str]] = [list(input()) for _ in range(R)]
delta_list: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def iterative_dfs():
    visited_alphabet = (1 << 27) - 1
    stack = [(0, 0, visited_alphabet, 0)]  # pos_x, pos_y, available_alphabet, count
    max_count = 0

    while stack:
        pos_x, pos_y, available_alphabet, count = stack.pop()
        alphabet_order = ord(graph[pos_y][pos_x]) - ord("A")
        
        if available_alphabet & (1 << alphabet_order):
            available_alphabet ^= (1 << alphabet_order)
            max_count = max(max_count, count + 1)
            
            for dx, dy in delta_list:
                new_x, new_y = pos_x + dx, pos_y + dy
                if 0 <= new_x < C and 0 <= new_y < R:
                    stack.append((new_x, new_y, available_alphabet, count + 1))
            
            available_alphabet ^= (1 << alphabet_order)

    return max_count

answer = iterative_dfs()
print(answer)