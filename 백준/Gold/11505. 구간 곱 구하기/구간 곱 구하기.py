# 11505 구간 곱 구하기

# 세그먼트 트리 구현체

from math import log2, ceil
from sys import stdin, stdout

mod = 10**9 + 7


class SegmentTree:
    """This class is for faster range queries and updates on a list.
    This class gets a list called "members" and does the tree building process in a seperate array called "tree".
    Then, it does the query and update in fittingly named function called "query" and "updates", respectively.
    Keep in mind that when calling "query" and "update", the index uses "ONE BASED NUMBERING" system(i.e. The initial element is assigned the index "1".) on the input, but the internal logic uses "ZERO BASED". (i.e. The initial element is assigned the index "0".)
    """

    def __init__(self, members: list[int]):
        # 어차피 필요한 멤버 갯수 빼고는 0으로 패딩 예정이라 깔끔하게 2의 승수가 될 수 있게 설정함
        self.member_count = len(members)
        self.tree_max_level = ceil(log2(self.member_count))
        self.tree_capacity = 1 << self.tree_max_level
        self.tree = [1 for _ in range(self.tree_capacity << 1)]
        self.build(members)

    def __str__(self, level: int = 0, pos: int = 1) -> str:
        indent: str = "    " * level
        left_string: str = (
            f"    {indent}L{level+1}={self.__str__(level=level+1, pos=2*pos)}"
            if 2 * pos < len(self.tree)
            else ""
        )
        right_string: str = (
            f"    {indent}R{level+1}={self.__str__(level=level+1, pos=2*pos+1)}"
            if 2 * pos + 1 < len(self.tree)
            else ""
        )
        if level == 0:
            return f"root={self.tree[pos]}\n{left_string}\n{right_string}"
        elif level == self.tree_max_level:
            return f"{self.tree[pos]}"
        else:
            return f"{self.tree[pos]}\n{left_string}\n{right_string}"

    def build(self, members: list[int]):
        for index, member in enumerate(members):
            self.tree[self.tree_capacity + index] = member
        for i in range(self.tree_capacity - 1, 0, -1):
            self.tree[i] = self.tree[2 * i + 0] * self.tree[2 * i + 1] % mod

    def update(self, index: int, value: int):
        """Keep in mind that the index uses "ONE BASED NUMBERING" system(i.e. The initial element is assigned the index "1".) on the input, but the internal logic uses "ZERO BASED". (i.e. The initial element is assigned the index "0".)"""
        next_index = self.tree_capacity + index - 1
        self.tree[next_index] = value
        next_index >>= 1
        while next_index:
            self.tree[next_index] = (
                self.tree[next_index * 2 + 0] * self.tree[next_index * 2 + 1] % mod
            )
            next_index >>= 1

    def query(self, index_start: int, index_end: int) -> int:
        """Keep in mind that the index uses "ONE BASED NUMBERING" system(i.e. The initial element is assigned the index "1".) on the input, but the internal logic uses "ZERO BASED". (i.e. The initial element is assigned the index "0".)"""
        index_start += self.tree_capacity - 1
        index_end += self.tree_capacity - 1
        result: int = 1
        while index_start <= index_end:
            if index_start % 2 == 1:
                result = result * self.tree[index_start] % mod
                index_start += 1
            if index_end % 2 == 0:
                result = result * self.tree[index_end] % mod
                index_end -= 1
            index_start >>= 1
            index_end >>= 1
        return result


N, M, K = (int(i) for i in stdin.readline().strip().split(" "))
my_segment_tree = SegmentTree([int(stdin.readline().strip()) for i in range(N)])
for _ in range(M + K):
    a, b, c = (int(i) for i in stdin.readline().strip().split(" "))
    if a == 1:
        my_segment_tree.update(b, c)
    elif a == 2:
        stdout.writelines(str(my_segment_tree.query(b, c)) + "\n")
