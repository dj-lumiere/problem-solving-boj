# 1987 알파벳
R, C = list(map(int, input().split(" ")))
graph = [list(map(lambda x: ord(x)-ord("A"), input())) for _ in range(R)]
delta_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def iterative_dfs():
    visited_alphabet = (1 << 26) - 1
    visited_bitmask = (1 << 26) - 1
    pos_bitmask = (1 << 5) - 1
    # C CCCC CCCC XXXX XYYY YYVV VVVV VVVV VVVV VVVV VVVV VVVV
    stack = [visited_alphabet]
    max_count = 0

    while stack:
        state = stack.pop()
        available_alphabet = state & visited_bitmask
        pos_y = (state >> 26) & pos_bitmask
        pos_x = (state >> 31) & pos_bitmask
        count = state >> 36
        alphabet_order = graph[pos_y][pos_x]
        
        if available_alphabet & (1 << alphabet_order):
            available_alphabet ^= (1 << alphabet_order)
            max_count = max(max_count, count + 1)
            
            for dx, dy in delta_list:
                new_x, new_y = pos_x + dx, pos_y + dy
                if 0 <= new_x < C and 0 <= new_y < R:
                    stack.append(((count + 1) << 36) + (new_x << 31) + (new_y << 26) + available_alphabet)
            
            available_alphabet ^= (1 << alphabet_order)

    return max_count

answer = iterative_dfs()
print(answer)