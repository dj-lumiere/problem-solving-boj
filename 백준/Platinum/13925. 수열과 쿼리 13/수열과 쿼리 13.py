from math import ceil, log2
from sys import stdout, stderr

MOD = 10**9+7


class SegmentTree:
    def __init__(self, initial_values, default_value = 0, base_index = 0):
        """Initializing essential parameters and arrays for segment tree and lazy propagation"""
        # Total number of elements in the initial array
        self.size = len(initial_values)
        # default value for tree nodes
        self.default_value = default_value
        # Value indicating no update is required
        self.no_update_value_a = 1
        self.no_update_value_b = 0
        # Height of the tree
        self.tree_height = ceil(log2(self.size))
        # Total size of the segment tree (power of 2)
        self.tree_size = 1 << self.tree_height
        # Base index for accessing elements in the segment tree
        self.base_index = base_index
        # The segment tree array
        self.tree = [self.default_value] * (2 * self.tree_size)
        # Array for lazy updates in multiply
        self.lazy_a = [self.no_update_value_a] * (2 * self.tree_size)
        self.lazy_b = [self.no_update_value_b] * (2 * self.tree_size)
        # Array to store the number of elements affected by lazy updates
        self.lazy_multiplier = [0] * (2 * self.tree_size)
        # Offset to adjust tree index calculations
        self.index_offset = self.tree_size - self.base_index
        # Build the segment tree with initial values
        self._build_tree(initial_values)

    def update_point(self, index, value_a, value_b, opcode):
        """Updates a single point in the segment tree"""
        index += self.index_offset
        for level in range(self.tree_height, 0, -1):
            self._propagate_update(index >> level)
        if opcode == "add":
            self._apply_update_add(index, value_a, value_b)
        if opcode == "mul":
            self._apply_update_mul(index, value_a, value_b)
        if opcode == "set":
            self._apply_update_set(index, value_a, value_b)
        for level in range(1, self.tree_height + 1):
            self._merge_children(index >> level)

    def update_range(self, left, right, value_a, value_b, opcode):
        """Updates a range of values in the segment tree with lazy propagation"""
        left += self.index_offset
        right += self.index_offset
        for level in range(self.tree_height, 0, -1):
            if ((left >> level) << level) != left:
                self._propagate_update(left >> level)
            if (((right + 1) >> level) << level) != right + 1:
                self._propagate_update(right >> level)
        L, R = left, right
        while L <= R:
            if L % 2 == 1:
                if opcode == "add":
                    self._apply_update_add(L, value_a, value_b)
                if opcode == "mul":
                    self._apply_update_mul(L, value_a, value_b)
                if opcode == "set":
                    self._apply_update_set(L, value_a, value_b)
                L += 1
            if R % 2 == 0:
                if opcode == "add":
                    self._apply_update_add(R, value_a, value_b)
                if opcode == "mul":
                    self._apply_update_mul(R, value_a, value_b)
                if opcode == "set":
                    self._apply_update_set(R, value_a, value_b)
                R -= 1
            L >>= 1
            R >>= 1
        for level in range(1, self.tree_height + 1):
            if ((left >> level) << level) != left:
                self._merge_children(left >> level)
            if (((right + 1) >> level) << level) != right + 1:
                self._merge_children(right >> level)

    def query_point(self, index):
        """Queries a single point from the segment tree, applying any pending lazy updates"""
        index += self.index_offset
        for level in range(self.tree_height, 0, -1):
            self._propagate_update(index >> level)
        return self.tree[index]

    def query_range(self, left, right):
        """Queries a range from the segment tree, applying any pending lazy updates"""
        left_result = self.default_value
        right_result = self.default_value
        left += self.index_offset
        right += self.index_offset
        for level in range(self.tree_height, 0, -1):
            if ((left >> level) << level) != left:
                self._propagate_update(left >> level)
            if (((right + 1) >> level) << level) != right + 1:
                self._propagate_update(right >> level)
        while left <= right:
            if left % 2 == 1:
                left_result = self._combine_node_values(left_result, self.tree[left])
                left += 1
            if right % 2 == 0:
                right_result = self._combine_node_values(self.tree[right], right_result)
                right -= 1
            left >>= 1
            right >>= 1
        return self._combine_node_values(left_result, right_result)

    def _build_tree(self, initial_values):
        """Builds the segment tree from initial values"""
        for i, v in enumerate(initial_values, start=self.tree_size):
            self.tree[i] = v
            self.lazy_a[i] = self.no_update_value_a
            self.lazy_b[i] = self.no_update_value_b
            self.lazy_multiplier[i] = 1
        for i in range(self.tree_size - 1, 0, -1):
            self._merge_children(i)

    def _apply_update_add(self, index, value_a, value_b):
        """Applies an update to a node in the tree and propagates the update lazily if needed"""
        self.tree[index] = self._apply_lazy_update_add(value_a, value_b, self.tree[index], self.lazy_multiplier[index])
        if index < self.tree_size:
            self.lazy_a[index] = self._accumulate_lazy_a_updates_add(value_a, value_b,
                                                                     self.lazy_a[index], self.lazy_b[index])
            self.lazy_b[index] = self._accumulate_lazy_b_updates_add(value_a, value_b,
                                                                     self.lazy_a[index], self.lazy_b[index])

    def _apply_update_mul(self, index, value_a, value_b):
        """Applies an update to a node in the tree and propagates the update lazily if needed"""
        self.tree[index] = self._apply_lazy_update_mul(value_a, value_b, self.tree[index], self.lazy_multiplier[index])
        if index < self.tree_size:
            self.lazy_a[index] = self._accumulate_lazy_a_updates_mul(value_a, value_b,
                                                                     self.lazy_a[index], self.lazy_b[index])
            self.lazy_b[index] = self._accumulate_lazy_b_updates_mul(value_a, value_b,
                                                                     self.lazy_a[index], self.lazy_b[index])

    def _apply_update_set(self, index, value_a, value_b):
        """Applies an update to a node in the tree and propagates the update lazily if needed"""
        self.tree[index] = self._apply_lazy_update_set(value_a, value_b, self.tree[index], self.lazy_multiplier[index])
        if index < self.tree_size:
            self.lazy_a[index] = self._accumulate_lazy_a_updates_set(value_a, value_b,
                                                                     self.lazy_a[index], self.lazy_b[index])
            self.lazy_b[index] = self._accumulate_lazy_b_updates_set(value_a, value_b,
                                                                     self.lazy_a[index], self.lazy_b[index])

    def _propagate_update(self, index):
        """Propagates lazy updates from the current node down to its children"""
        self._apply_update_add(2 * index, self.lazy_a[index], self.lazy_b[index])
        self._apply_update_add(2 * index + 1, self.lazy_a[index], self.lazy_b[index])
        self.lazy_a[index] = self.no_update_value_a
        self.lazy_b[index] = self.no_update_value_b

    def _merge_children(self, index):
        """Combines the values of children nodes to update the parent node"""
        self.tree[index] = self._combine_node_values(self.tree[2 * index], self.tree[2 * index + 1])
        self.lazy_multiplier[index] = (self.lazy_multiplier[2 * index] + self.lazy_multiplier[2 * index + 1])

    def __str__(self, level: int = 0, pos: int = 1):
        """Returns a string representation of the segment tree for debugging purposes"""
        indent = "    " * level
        left_string = (
            f"    {indent}L{level + 1}={self.__str__(level=level + 1, pos=2 * pos)}" if 2 * pos < len(self.tree) else "")
        right_string = (
            f"    {indent}R{level + 1}={self.__str__(level=level + 1, pos=2 * pos + 1)}" if 2 * pos + 1 < len(self.tree) else "")
        if level == 0:
            return f"root={self.tree[pos]} ({self.lazy_a[pos]}x+{self.lazy_b[pos]})\n{left_string}\n{right_string}"
        elif level == self.tree_height:
            return f"{self.tree[pos]} ({self.lazy_a[pos]}x+{self.lazy_b[pos]})"
        else:
            return f"{self.tree[pos]} ({self.lazy_a[pos]}x+{self.lazy_b[pos]})\n{left_string}\n{right_string}"

    def _combine_node_values(self, left, right):
        """Combines the values of two nodes
        This method is dependent on the specific use-case of the segment tree"""
        # Change this part for various operations
        return (left + right) % MOD

    def _apply_lazy_update_add(self, lazy_value_a, lazy_value_b, node_value, lazy_multiplier):
        """Applies a lazy update to a node
        This method should be modified based on the use-case"""
        # Change this part for various operations
        return (lazy_value_a * node_value + lazy_value_b * lazy_multiplier) % MOD

    def _apply_lazy_update_mul(self, lazy_value_a, lazy_value_b, node_value, lazy_multiplier):
        """Applies a lazy update to a node
        This method should be modified based on the use-case"""
        # Change this part for various operations
        return (lazy_value_a * node_value + lazy_value_b * lazy_multiplier) % MOD

    def _apply_lazy_update_set(self, lazy_value_a, lazy_value_b, node_value, lazy_multiplier):
        """Applies a lazy update to a node
        This method should be modified based on the use-case"""
        # Change this part for various operations
        if lazy_value_a == self.no_update_value_a and lazy_value_b == self.no_update_value_b:
            return node_value
        return lazy_value_b * lazy_multiplier

    def _accumulate_lazy_a_updates_add(self, lazy_value1_a, lazy_value1_b, lazy_value2_a, lazy_value2_b):
        """Accumulates lazy update values
        This method is to be customized based on the specific use-case"""
        # Change this part for various operations
        return lazy_value1_a * lazy_value2_a % MOD

    def _accumulate_lazy_b_updates_add(self, lazy_value1_a, lazy_value1_b, lazy_value2_a, lazy_value2_b):
        """Accumulates lazy update values
        This method is to be customized based on the specific use-case"""
        # Change this part for various operations
        return (lazy_value1_b + lazy_value2_b * lazy_value1_a) % MOD

    def _accumulate_lazy_a_updates_mul(self, lazy_value1_a, lazy_value1_b, lazy_value2_a, lazy_value2_b):
        """Accumulates lazy update values
        This method is to be customized based on the specific use-case"""
        # Change this part for various operations
        return lazy_value1_a * lazy_value2_a % MOD

    def _accumulate_lazy_b_updates_mul(self, lazy_value1_a, lazy_value1_b, lazy_value2_a, lazy_value2_b):
        """Accumulates lazy update values
        This method is to be customized based on the specific use-case"""
        # Change this part for various operations
        return (lazy_value1_b + lazy_value2_b * lazy_value1_a) % MOD

    def _accumulate_lazy_a_updates_set(self, lazy_value1_a, lazy_value1_b, lazy_value2_a, lazy_value2_b):
        """Accumulates lazy update values
        This method is to be customized based on the specific use-case"""
        # Change this part for various operations
        return 0

    def _accumulate_lazy_b_updates_set(self, lazy_value1_a, lazy_value1_b, lazy_value2_a, lazy_value2_b):
        """Accumulates lazy update values
        This method is to be customized based on the specific use-case"""
        # Change this part for various operations
        return (lazy_value1_a * lazy_value2_a + lazy_value1_b) % MOD


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    t = 1
    answers = []
    for h in range(t):
        n = int(input())
        numbers = [int(input()) for _ in range(n)]
        m = int(input())
        segment_tree = SegmentTree(numbers, 0, 1)
        for i in range(m):
            opcode = int(input())
            if opcode == 1:
                x, y, v = (int(input()) for _ in range(3))
                segment_tree.update_range(x, y, 1, v, "add")
            if opcode == 2:
                x, y, v = (int(input()) for _ in range(3))
                segment_tree.update_range(x, y, v, 0, "mul")
            if opcode == 3:
                x, y, v = (int(input()) for _ in range(3))
                segment_tree.update_range(x, y, 0, v, "set")
            if opcode == 4:
                x, y = (int(input()) for _ in range(2))
                answers.append(f"{segment_tree.query_range(x, y)}")
    print(*answers, sep="\n")