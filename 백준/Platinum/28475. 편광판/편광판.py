from bisect import bisect_left, bisect_right
from itertools import product
from math import ceil, log2
from sys import stdout, stderr


class SegmentTree:
    def __init__(self, members, default, index_start):
        # 어차피 필요한 멤버 갯수 빼고는 0으로 패딩 예정이라 깔끔하게 2의 승수가 될 수 있게 설정함
        self.member_count = len(members)
        self.default = default
        self.tree_max_level = ceil(log2(self.member_count))
        self.tree_capacity = 1 << self.tree_max_level
        self.tree = [self.default for _ in range(self.tree_capacity << 1)]
        self.index_offset = self.tree_capacity - index_start
        self.build(members)

    def __str__(self, level: int = 0, pos: int = 1) -> str:
        indent: str = "    " * level
        left_string: str = (
            f"    {indent}L{level + 1}={self.__str__(level=level + 1, pos=2 * pos)}"
            if 2 * pos < len(self.tree)
            else ""
        )
        right_string: str = (
            f"    {indent}R{level + 1}={self.__str__(level=level + 1, pos=2 * pos + 1)}"
            if 2 * pos + 1 < len(self.tree)
            else ""
        )
        if level == 0:
            return f"root={self.tree[pos]}\n{left_string}\n{right_string}"
        elif level == self.tree_max_level:
            return f"{self.tree[pos]}"
        else:
            return f"{self.tree[pos]}\n{left_string}\n{right_string}"

    def build(self, members):
        for index, member in enumerate(members):
            self.tree[self.tree_capacity + index] = member
        for i in range(self.tree_capacity - 1, 0, -1):
            self.tree[i] = self.merge_nodes(self.tree[i * 2], self.tree[i * 2 + 1])

    def update(self, index, value):
        """Keep in mind that the index uses "ZERO BASED NUMBERING" system. (i.e. The initial element is assigned the index "0".)"""
        next_index = self.index_offset + index
        self.tree[next_index] = value
        while next_index:
            next_index >>= 1
            self.tree[next_index] = self.merge_nodes(self.tree[next_index * 2], self.tree[next_index * 2 + 1])

    def query(self, index_start, index_end):
        """Keep in mind that the index uses "ZERO BASED NUMBERING" system. (i.e. The initial element is assigned the index "0".)"""
        index_start += self.index_offset
        index_end += self.index_offset
        index_end += 1
        result = self.default
        numbers = [index_start]
        first_target = 1 << (index_end.bit_length() - 1)
        for i in range(index_end.bit_length() - 1):
            if index_start & (1 << i) != 0 and (index_start + (1 << i) <= index_end):
                index_start += 1 << i
                numbers.append(index_start)
        if index_start == 0:
            numbers.append(first_target)
            index_start = first_target
        for i in range(index_end.bit_length() - 2, -1, -1):
            if index_end & (1 << i) != 0 and index_start & (1 << i) == 0:
                index_start += 1 << i
                numbers.append(index_start)
        for left, right in zip(numbers, numbers[1:]):
            shift_length = (right - left).bit_length() - 1
            result = self.merge_nodes(result, self.tree[left >> shift_length])
        return result

    def merge_nodes(self, left, right):
        # Change this part for various operations
        left_start = left >> 4
        left_end = left & 15
        right_start = right >> 4
        right_end = right & 15
        current_light = left_start
        for a, i in enumerate([left_end, right_start, right_end]):
            if i == LIGHT_UNBLOCKED:
                continue
            if i == LIGHT_BLOCKED:
                current_light = LIGHT_BLOCKED
                break
            if current_light == LIGHT_UNBLOCKED:
                current_light = i
                continue
            if a == 1 and any(current_light & (1 << j) != 0 and i & (1 << ((j + 2) & 3)) != 0 for j in range(4)):
                current_light = LIGHT_BLOCKED
                break
            current_light = i
        return (left_start << 4) + current_light


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    LIGHT_UNBLOCKED = 15
    LIGHT_BLOCKED = 0
    LIGHT_STATE = [1, 2, 4, 8]
    answers = []
    for hh in range(t):
        n, m = (int(input()) for _ in range(2))
        a = [int(input()) for _ in range(n)]
        st = SegmentTree(
            [(LIGHT_STATE[v & 3] << 4) + LIGHT_STATE[v & 3] for v in a],
            default=(LIGHT_UNBLOCKED << 4) + LIGHT_UNBLOCKED,
            index_start=1
        )
        for _ in range(m):
            q, a, b = (int(input()) for _ in range(3))
            if q == 1:
                st.update(a, (LIGHT_STATE[b & 3] << 4) + LIGHT_STATE[b & 3])
            if q == 2:
                light_ray = st.query(a, b)
                answer = int(light_ray & 15 != LIGHT_BLOCKED)
                answers.append(f"{answer}")
    print(*answers, sep="\n")
