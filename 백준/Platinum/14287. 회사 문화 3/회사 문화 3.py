# 14288 회사 문화 4
import io
import os
from array import array
from math import ceil, log2


class SegmentTree:
    def __init__(self, members, default=0, identity=0, index_start=0):
        self.size = len(members)
        self.default = default
        self.identity = identity
        self.log_size = ceil(log2(self.size))
        self.tree_capacity = 1 << self.log_size
        self.index_start = index_start
        self.tree = array('I', [self.default] * (2 * self.tree_capacity))
        self.lazy = array('I', [self.identity] * (2 * self.tree_capacity))
        self.lazy_multiplier = array('I', [0] * (2 * self.tree_capacity))
        self.index_offset = self.tree_capacity - self.index_start
        self.build_tree(members)

    def build_tree(self, members):
        for i, v in enumerate(members, start=self.tree_capacity):
            self.tree[i] = v
            self.lazy_multiplier[i] = 1
        for i in range(self.tree_capacity - 1, 0, -1):
            self.pull(i)

    def point_update(self, index, value):
        index += self.index_offset
        for level in range(self.log_size, 0, -1):
            self.push(index >> level)
        self.apply_update(index, value)
        for level in range(1, self.log_size + 1):
            self.pull(index >> level)

    def range_update(self, left, right, value):
        left += self.index_offset
        right += self.index_offset
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

    def point_query(self, index):
        index += self.index_offset
        for level in range(self.log_size, 0, -1):
            self.push(index >> level)
        return self.tree[index]

    def range_query(self, left, right):
        left_result = self.default
        right_result = self.default
        left += self.index_offset
        right += self.index_offset
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
        self.tree[index] = self.update_node(value, self.tree[index], self.lazy_multiplier[index])
        if index < self.tree_capacity:
            self.lazy[index] = self.compose_lazies(value, self.lazy[index])

    def push(self, index):
        self.apply_update(2 * index, self.lazy[index])
        self.apply_update(2 * index + 1, self.lazy[index])
        self.lazy[index] = self.identity

    def pull(self, index):
        self.tree[index] = self.merge_nodes(self.tree[2 * index], self.tree[2 * index + 1])
        self.lazy_multiplier[index] = (self.lazy_multiplier[2 * index] + self.lazy_multiplier[2 * index + 1])

    def merge_nodes(self, left, right):
        return left + right

    def update_node(self, lazy_value, node_value, lazy_multiplier):
        return node_value + lazy_value * lazy_multiplier

    def compose_lazies(self, lazy_value1, lazy_value2):
        return lazy_value1 + lazy_value2


def dfs(root, graph, size):
    time = 0
    stack = [(root, False)]
    time_in = array('I', [0 for _ in range(size + 1)])
    time_out = array('I', [0 for _ in range(size + 1)])
    while stack:
        node, visited = stack.pop()
        if not visited:
            time += 1
            time_in[node] = time
            stack.append((node, True))
            for child in reversed(graph[node]):
                if time_in[child] == 0:
                    stack.append((child, False))
        else:
            time_out[node] = time
    return time_in, time_out


TOWARD_BOSS = 1
TOWARD_SUBORDINATE = 0
tokens = iter(os.read(0, os.fstat(0).st_size).split())
N, M = int(next(tokens)), int(next(tokens))
last_node = array('i', [int(next(tokens)) for _ in range(N)])
graph = [[] for _ in range(N + 1)]
for i, v in enumerate(last_node, start=1):
    if i == 1:
        continue
    graph[v].append(i)
    graph[i].append(v)
time_in, time_out = dfs(root=1, graph=graph, size=N)

segment_tree = SegmentTree(members=[0] * N, default=0, identity=0, index_start=1)
segment_tree2 = SegmentTree(members=[0] * N, default=0, identity=0, index_start=1)
current_direction = TOWARD_BOSS
answer = array('I')

# Process the operations
for _ in range(M):
    opcode = int(next(tokens))

    # Update operation
    if opcode == 1:
        starting_member, value = int(next(tokens)), int(next(tokens))
        start = time_in[starting_member]
        end = time_out[starting_member]
        if current_direction == TOWARD_SUBORDINATE:
            segment_tree.range_update(start, end, value)
        elif current_direction == TOWARD_BOSS:
            segment_tree2.point_update(start, value)

    # Query operation
    if opcode == 2:
        starting_member = int(next(tokens))
        start = time_in[starting_member]
        end = time_out[starting_member]
        result = segment_tree.point_query(start) + segment_tree2.range_query(start, end)
        answer.append(result)

    if opcode == 3:
        if current_direction == TOWARD_SUBORDINATE:
            current_direction = TOWARD_BOSS
        else:
            current_direction = TOWARD_SUBORDINATE

os.write(1, "\n".join(map(str, answer)).encode())