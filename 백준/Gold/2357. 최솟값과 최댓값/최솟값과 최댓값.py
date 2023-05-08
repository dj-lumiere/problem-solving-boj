# 10868 최솟값

# 세그먼트 트리 구현체

from math import log2, ceil
from sys import stdin, stdout


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
        self.min_tree = [0 for _ in range(self.tree_capacity << 1)]
        self.max_tree = [0 for _ in range(self.tree_capacity << 1)]
        self.build(members)

    def build(self, members: list[int]):
        for index, member in enumerate(members):
            self.min_tree[self.tree_capacity + index] = member
            self.max_tree[self.tree_capacity + index] = member
        for i in range(self.tree_capacity - 1, 0, -1):
            self.min_tree[i] = min(self.min_tree[2 * i + 0], self.min_tree[2 * i + 1])
            self.max_tree[i] = max(self.max_tree[2 * i + 0], self.max_tree[2 * i + 1])

    def query(self, index_start: int, index_end: int) -> str:
        """Keep in mind that the index uses "ZERO BASED NUMBERING" system. (i.e. The initial element is assigned the index "0".)"""
        index_start += self.tree_capacity - 1
        index_end += self.tree_capacity - 1
        result_min: int = 10000000000
        result_max: int = -10000000000
        while index_start <= index_end:
            if index_start % 2 == 1:
                result_min = min(result_min, self.min_tree[index_start])
                result_max = max(result_max, self.max_tree[index_start])
                index_start += 1
            if index_end % 2 == 0:
                result_min = min(result_min, self.min_tree[index_end])
                result_max = max(result_max, self.max_tree[index_end])
                index_end -= 1
            index_start >>= 1
            index_end >>= 1
        return f"{result_min} {result_max}"


N, M = (int(i) for i in stdin.readline().strip().split(" "))
my_segment_tree = SegmentTree([int(stdin.readline().strip()) for i in range(N)])
for _ in range(M):
    a, b = (int(i) for i in stdin.readline().strip().split(" "))
    stdout.writelines(str(my_segment_tree.query(a, b)) + "\n")
