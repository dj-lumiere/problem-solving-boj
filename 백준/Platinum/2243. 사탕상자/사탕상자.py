# 2243 사탕 상자

from math import log2, ceil
from sys import stdin


def input():
    return stdin.readline().strip()


class SegmentTree:
    """This class is for faster range queries and updates on a list.
    This class gets a list called "members" and does the tree building process in a seperate array called "tree".
    Then, it does the query and update in fittingly named function called "query" and "updates", respectively.
    Keep in mind that when calling "query" and "update", the index uses "ZERO BASED NUMBERING" system.
    """

    def __init__(self, members: list[int]):
        # 어차피 필요한 멤버 갯수 빼고는 0으로 패딩 예정이라 깔끔하게 2의 승수가 될 수 있게 설정함
        self.member_count = len(members)
        self.tree_max_level = ceil(log2(self.member_count))
        self.tree_capacity = 1 << self.tree_max_level
        self.tree = [0 for _ in range(self.tree_capacity << 1)]
        self.build(members)

    def build(self, members: list[int]):
        for index, member in enumerate(members):
            self.tree[self.tree_capacity + index] = member
        for i in range(self.tree_capacity - 1, 0, -1):
            self.tree[i] = self.tree[2 * i + 0] + self.tree[2 * i + 1]

    def update(self, index: int, value: int):
        next_index = self.tree_capacity + index - 1
        self.tree[next_index] += value
        next_index >>= 1
        while next_index:
            self.tree[next_index] = (
                self.tree[next_index * 2 + 0] + self.tree[next_index * 2 + 1]
            )
            next_index >>= 1

    def query(self, index_start: int, index_end: int) -> int:
        index_start += self.tree_capacity - 1
        index_end += self.tree_capacity - 1
        result: int = 0
        while index_start <= index_end:
            if index_start % 2 == 1:
                result += self.tree[index_start]
                index_start += 1
            if index_end % 2 == 0:
                result += self.tree[index_end]
                index_end -= 1
            index_start >>= 1
            index_end >>= 1
        return result

    def nth_element_value(self, n):
        index = 1
        next_number = n
        while index < self.tree_capacity:
            if next_number > self.tree[index * 2]:
                next_number -= self.tree[index * 2]
                index = index * 2 + 1
            else:
                index = index * 2
        return index - self.tree_capacity

    def __str__(self) -> str:
        dfs_stack: list[tuple[int, int]] = [(0, 1)]
        result: list[str] = []
        while dfs_stack:
            level, pos = dfs_stack.pop()
            if pos >= self.tree_capacity * 2:
                continue
            indent: str = "    " * level
            if level == self.tree_max_level:
                member_index: int = pos - self.tree_capacity
                result.append(
                    f"{indent}member{member_index+1}[index={pos}]={self.tree[pos]}"
                )
            elif level == 0:
                result.append(f"root[index={pos}]={self.tree[pos]}")
            else:
                if not pos % 2:
                    result.append(f"{indent}L{level}[index={pos}]={self.tree[pos]}")
                else:
                    result.append(f"{indent}R{level}[index={pos}]={self.tree[pos]}")
            dfs_stack.append((level + 1, 2 * pos + 1))
            dfs_stack.append((level + 1, 2 * pos))
        return "\n".join(result)


n = int(input())
candy_taste_count = SegmentTree([0] * 10**6)
for _ in range(n):
    operator, *operand = map(int, input().split(" "))
    if operator == 1:
        B = operand[0]
        result = candy_taste_count.nth_element_value(B) + 1
        print(result)
        candy_taste_count.update(result, -1)
    if operator == 2:
        B, C = operand
        candy_taste_count.update(B, C)