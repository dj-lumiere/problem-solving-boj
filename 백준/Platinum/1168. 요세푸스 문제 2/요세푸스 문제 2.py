from os import write
from math import comb, cos, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau


class SegmentTree:
    """This class is for faster range queries and updates on a list.
    This class gets a list called "members" and does the tree building process in a seperate array called "tree".
    Then, it does the query and update in fittingly named function called "query" and "updates", respectively.
    Keep in mind that when calling "query" and "update", the index uses "ZERO BASED NUMBERING" system.
    """

    def __init__(self, members, index_start=0):
        # 어차피 필요한 멤버 갯수 빼고는 0으로 패딩 예정이라 깔끔하게 2의 승수가 될 수 있게 설정함
        self.member_count = len(members)
        self.tree_max_level = ceil(log2(self.member_count))
        self.tree_capacity = 1 << self.tree_max_level
        self.tree = [0 for _ in range(self.tree_capacity << 1)]
        self.index_start = index_start
        self.index_offset = self.tree_capacity - self.index_start
        self.build(members)

    def build(self, members):
        for index, member in enumerate(members):
            self.tree[self.tree_capacity + index] = member
        for i in range(self.tree_capacity - 1, 0, -1):
            self.tree[i] = self.tree[2 * i + 0] + self.tree[2 * i + 1]

    def update(self, index, value):
        next_index = index + self.index_offset
        self.tree[next_index] += value
        next_index >>= 1
        while next_index:
            self.tree[next_index] = (self.tree[next_index * 2 + 0] + self.tree[next_index * 2 + 1])
            next_index >>= 1

    def query(self, index_start, index_end):
        index_start += self.index_offset
        index_end += self.index_offset
        result = 0
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

    def __str__(self):
        dfs_stack = [(0, 1)]
        result = []
        while dfs_stack:
            level, pos = dfs_stack.pop()
            if pos >= self.tree_capacity * 2:
                continue
            indent: str = "    " * level
            if level == self.tree_max_level:
                member_index: int = pos - self.tree_capacity
                result.append(f"{indent}member{member_index + 1}[index={pos}]={self.tree[pos]}")
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


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="\n": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep=" ", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        k = int(input())
        result = [0]
        killed = [False for _ in range(n + 1)]
        killed[0] = True
        my_segtree = SegmentTree([1] * (2 * n), index_start=1)
        target_order = k
        for i in reversed(range(2, n + 1)):
            if i < k:
                target_order = (k - 1) % i + 1
            start = 0
            end = 2 * n + 1 - result[-1]
            while start + 1 < end:
                mid = (start + end) // 2
                q_start = result[-1] + 1
                q_end = q_start + mid
                current_count = my_segtree.query(q_start, q_end)
                if current_count > target_order or (
                        current_count == target_order and my_segtree.query(q_end, q_end) == 0):
                    end = mid
                else:
                    start = mid
            next_kill = (result[-1] + end - 1) % n + 1
            killed[next_kill] = True
            result.append(next_kill)
            my_segtree.update(next_kill, -1)
            my_segtree.update(next_kill + n, -1)
        last_one = 0
        for i, v in enumerate(killed):
            if not v:
                last_one = i
        result.append(last_one)
        answer = "<" + ", ".join(map(str, result[1:])) + ">"
        answers.append(f"{answer}")
    print(*answers, sep="\n")