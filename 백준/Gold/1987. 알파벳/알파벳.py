# 1987 알파벳

R, C = list(map(int, input().split(" ")))
graph: list[list[str]] = [list(input()) for _ in range(R)]
delta_list: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(
    pos_x: int,
    pos_y: int,
    available_alphabet: int,
    available_alphabet_count: int,
) -> int:
    alphabet_order = ord(graph[pos_y][pos_x]) - ord("A")
    if available_alphabet & (1 << alphabet_order):
        available_alphabet = available_alphabet ^ (1 << alphabet_order)
        max_count: int = 0
        for i, j in delta_list:
            new_x = pos_x + i
            new_y = pos_y + j
            if 0 <= new_x < C and 0 <= new_y < R:
                count = dfs(
                    pos_x=pos_x + i,
                    pos_y=pos_y + j,
                    available_alphabet=available_alphabet,
                    available_alphabet_count=available_alphabet_count + 1,
                )
                max_count = max(max_count, count)
        available_alphabet = available_alphabet ^ (1 << alphabet_order)
        return max_count
    else:
        return available_alphabet_count


visited_alphabet: int = (1 << 27) - 1
answer: int = dfs(
    pos_x=0,
    pos_y=0,
    available_alphabet=visited_alphabet,
    available_alphabet_count=0,
)
print(answer)