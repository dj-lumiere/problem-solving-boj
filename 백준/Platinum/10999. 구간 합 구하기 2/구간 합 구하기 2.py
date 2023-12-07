# 10999 구간 합 구하기 2


# 10999 구간 합 구하기 2

from sys import stdin


class LazySegmentTree:
    def __init__(self, size=0, initial_value=None, identity_value=None):
        self.size = size
        self.initial_value = initial_value
        self.identity_value = identity_value
        self.log_size = self.calculate_log2(size)
        self.tree_capacity = 1 << self.log_size
        self.tree = [self.initial_value] * (2 * self.tree_capacity)
        self.lazy = [self.identity_value] * (2 * self.tree_capacity)
        self.lazy_multiplier = [0] * (2 * self.tree_capacity)

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
            return f"root={self.tree[pos]} ({self.lazy[pos]})\n{left_string}\n{right_string}"
        elif level == self.log_size:
            return f"{self.tree[pos]} ({self.lazy[pos]})"
        else:
            return f"{self.tree[pos]} ({self.lazy[pos]})\n{left_string}\n{right_string}"

    @staticmethod
    def calculate_log2(n):
        log_value = 0
        while n > (1 << log_value):
            log_value += 1
        return log_value

    def merge_nodes(self, left, right):
        return left + right

    def update_node(self, lazy_value, node_value, lazy_multiplier):
        return node_value + lazy_value * lazy_multiplier

    def compose_lazies(self, lazy_value1, lazy_value2):
        return lazy_value1 + lazy_value2

    def set_node_value(self, index, value):
        index = (index - 1) + self.tree_capacity
        self.tree[index] = value
        self.lazy_multiplier[index] = 1

    def initialize(self):
        for i in range(self.tree_capacity - 1, 0, -1):
            self.pull(i)

    def point_update(self, index, value):
        index = (index - 1) + self.tree_capacity
        for level in range(self.log_size, 0, -1):
            self.push(index >> level)
        self.apply_update(index, value)
        for level in range(1, self.log_size + 1):
            self.pull(index >> level)

    def range_update(self, left, right, value):
        left = (left - 1) + self.tree_capacity
        right = (right - 1) + self.tree_capacity
        for level in range(self.log_size, 0, -1):
            if ((left >> level) << level) != left:
                self.push(left >> level)
            if (((right + 1) >> level) << level) != right + 1:
                self.push(right >> level)
        L, R = left, right
        while L <= R:
            if L % 2 == 1:
                self.apply_update(L, value)
                L += 1
            if R % 2 == 0:
                self.apply_update(R, value)
                R -= 1
            L >>= 1
            R >>= 1
        for level in range(1, self.log_size + 1):
            if ((left >> level) << level) != left:
                self.pull(left >> level)
            if (((right + 1) >> level) << level) != right + 1:
                self.pull(right >> level)

    def query_point(self, index):
        index = (index - 1) + self.tree_capacity
        for level in range(self.log_size, 0, -1):
            self.push(index // (1 << level))
        return self.tree[index]

    def query_range(self, left, right):
        left_result = self.initial_value
        right_result = self.initial_value
        left = (left - 1) + self.tree_capacity
        right = (right - 1) + self.tree_capacity
        for level in range(self.log_size, 0, -1):
            if ((left >> level) << level) != left:
                self.push(left >> level)
            if (((right + 1) >> level) << level) != right + 1:
                self.push(right >> level)
        while left <= right:
            if left % 2 == 1:
                left_result = self.merge_nodes(left_result, self.tree[left])
                left += 1
            if right % 2 == 0:
                right_result = self.merge_nodes(self.tree[right], right_result)
                right -= 1
            left >>= 1
            right >>= 1
        return self.merge_nodes(left_result, right_result)

    def apply_update(self, index, value):
        self.tree[index] = self.update_node(
            value, self.tree[index], self.lazy_multiplier[index]
        )
        if index < self.tree_capacity:
            self.lazy[index] = self.compose_lazies(value, self.lazy[index])

    def push(self, index):
        self.apply_update(2 * index, self.lazy[index])
        self.apply_update(2 * index + 1, self.lazy[index])
        self.lazy[index] = self.identity_value

    def pull(self, index):
        self.tree[index] = self.merge_nodes(
            self.tree[2 * index], self.tree[2 * index + 1]
        )
        self.lazy_multiplier[index] = (
            self.lazy_multiplier[2 * index] + self.lazy_multiplier[2 * index + 1]
        )


def input():
    return stdin.readline().strip()


N, M, K = map(int, input().split(" "))
segment_tree = LazySegmentTree(size=N, initial_value=0, identity_value=0)
# Set the initial values
for i in range(1, N + 1):
    val = int(input())
    segment_tree.set_node_value(i, val)

segment_tree.initialize()

# Process the operations
for _ in range(M + K):
    opcode, *operand = list(map(int, input().split()))

    # Update operation
    if opcode == 1:
        start, end, value = operand
        segment_tree.range_update(start, end, value)

    # Query operation
    if opcode == 2:
        start, end = operand
        print(segment_tree.query_range(start, end))