# 14427 수열과 쿼리 15

from math import log2, ceil
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


print = stdout.write


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
        self.tree = [10**10 for _ in range(self.tree_capacity << 1)]
        self.tree2 = [0 for _ in range(self.tree_capacity << 1)]
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
            self.tree2[self.tree_capacity + index] = index + 1
        for i in range(self.tree_capacity - 1, 0, -1):
            self.tree[i] = min(self.tree[2 * i + 0], self.tree[2 * i + 1])
            if self.tree[2 * i + 0] == self.tree[2 * i + 1]:
                self.tree2[i] = min(self.tree2[2 * i + 0], self.tree2[2 * i + 1])
                continue
            if (
                self.tree[2 * i + 0] != self.tree[2 * i + 1]
                and self.tree[i] == self.tree[2 * i + 1]
            ):
                self.tree2[i] = self.tree2[2 * i + 1]
            if (
                self.tree[2 * i + 0] != self.tree[2 * i + 1]
                and self.tree[i] == self.tree[2 * i]
            ):
                self.tree2[i] = self.tree2[2 * i]

    def update(self, index: int, value: int):
        """Keep in mind that the index uses "ZERO BASED NUMBERING" system. (i.e. The initial element is assigned the index "0".)"""
        next_index = self.tree_capacity + index - 1
        self.tree[next_index] = value
        next_index >>= 1
        while next_index:
            self.tree[next_index] = min(
                self.tree[next_index * 2 + 0], self.tree[next_index * 2 + 1]
            )
            if self.tree[2 * next_index + 0] == self.tree[2 * next_index + 1]:
                self.tree2[next_index] = min(
                    self.tree2[2 * next_index + 0], self.tree2[2 * next_index + 1]
                )
            if (
                self.tree[2 * next_index + 0] != self.tree[2 * next_index + 1]
                and self.tree[next_index] == self.tree[next_index * 2 + 1]
            ):
                self.tree2[next_index] = self.tree2[2 * next_index + 1]
            if (
                self.tree[2 * next_index + 0] != self.tree[2 * next_index + 1]
                and self.tree[next_index] == self.tree[2 * next_index]
            ):
                self.tree2[next_index] = self.tree2[2 * next_index]
            next_index >>= 1

    def query(self, index_start: int, index_end: int) -> int:
        """Keep in mind that the index uses "ZERO BASED NUMBERING" system. (i.e. The initial element is assigned the index "0".)"""
        index_start += self.tree_capacity - 1
        index_end += self.tree_capacity - 1
        result: int = 10000000000
        index: int = 10000000000
        # print(
        #     f"ORIGINAL    -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16\nLEVEL       -  0  1  1  2  2  2  2  3  3  3  3  3  3  3  3  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4\nANCESTOR    -  -  1  1  2  2  3  3  4  4  5  5  6  6  7  7  8  8  9  9 10 10 11 11 12 12 13 13 14 14 15 15\nNODE        0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31\n"
        # )
        # print(f"{self.tree =}\n{self.tree2=}\n")
        while index_start <= index_end:
            # print(f"{index_start=} {index_end=} {result=} {index=}\n")
            if index_start % 2 == 1:
                if result > self.tree[index_start]:
                    result = self.tree[index_start]
                    index = self.tree2[index_start]
                elif result == self.tree[index_start]:
                    index = min(self.tree2[index_start], index)
                index_start += 1
            if index_end % 2 == 0:
                if result > self.tree[index_end]:
                    result = self.tree[index_end]
                    index = self.tree2[index_end]
                elif result == self.tree[index_end]:
                    index = min(self.tree2[index_end], index)
                index_end -= 1
            index_start >>= 1
            index_end >>= 1
        return index


N = int(input())
my_segment_tree = SegmentTree([int(i) for i in input().split(" ")])
M = int(input())
for _ in range(M):
    operator, *operand = (int(i) for i in input().split(" "))
    if operator == 1:
        my_segment_tree.update(*operand)
    elif operator == 2:
        query_result = my_segment_tree.query(1, N)
        print(f"{query_result}\n")