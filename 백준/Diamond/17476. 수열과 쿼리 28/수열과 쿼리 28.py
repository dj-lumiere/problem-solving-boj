from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit, stdout, stderr
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import cos, isqrt, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau


class SegmentTreeBeats:
    """https://judge.yosupo.jp/submission/232969"""
    POS_INF = 1 << 60  # Positive infinity
    NEG_INF = -POS_INF  # Negative infinity

    def __init__(self, n: int, iterable):
        self.n = n
        self.log = (n - 1).bit_length()
        self.tree_size = size = 1 << self.log
        total_size = 2 * size
        self.max_value = [self.NEG_INF] * total_size  # Maximum value in the segment
        self.second_max_value = [self.NEG_INF] * total_size  # Second maximum value
        self.max_count = [0] * total_size  # Count of maximum values
        self.min_value = [self.POS_INF] * total_size  # Minimum value in the segment
        self.second_min_value = [self.POS_INF] * total_size  # Second minimum value
        self.min_count = [0] * total_size  # Count of minimum values
        self.segment_sum = [0] * total_size  # Sum of the segment
        self.pending_addition = [0] * total_size  # Lazy addition
        self.pending_update = [self.POS_INF] * total_size  # Lazy set updates
        self.left_bound = [0] * size  # Left index of segment
        self.right_bound = [0] * size  # Right index of segment
        self.left_bound.extend(range(size))
        self.right_bound.extend(range(1, size + 1))

        # Build the segment tree structure
        for i in range(size - 1, 0, -1):
            self.left_bound[i] = self.left_bound[i << 1]
            self.right_bound[i] = self.right_bound[(i << 1) + 1]

        # Initialize leaves
        for i, a in enumerate(iterable, size):
            self.max_value[i] = self.min_value[i] = a
            self.segment_sum[i] = a
            self.max_count[i] = self.min_count[i] = 1
        # Build internal nodes
        for i in range(size - 1, 0, -1):
            self._merge(i)

    def _merge(self, k: int):
        """Merge the information from the child nodes into the parent node."""
        left, right = 2 * k, 2 * k + 1
        self.segment_sum[k] = self.segment_sum[left] + self.segment_sum[right]
        # Merge maximum values
        if self.max_value[left] > self.max_value[right]:
            self.max_value[k] = self.max_value[left]
            self.max_count[k] = self.max_count[left]
            self.second_max_value[k] = max(self.second_max_value[left], self.max_value[right])
        elif self.max_value[left] < self.max_value[right]:
            self.max_value[k] = self.max_value[right]
            self.max_count[k] = self.max_count[right]
            self.second_max_value[k] = max(self.max_value[left], self.second_max_value[right])
        else:
            self.max_value[k] = self.max_value[left]
            self.max_count[k] = self.max_count[left] + self.max_count[right]
            self.second_max_value[k] = max(self.second_max_value[left], self.second_max_value[right])
        # Merge minimum values
        if self.min_value[left] < self.min_value[right]:
            self.min_value[k] = self.min_value[left]
            self.min_count[k] = self.min_count[left]
            self.second_min_value[k] = min(self.second_min_value[left], self.min_value[right])
        elif self.min_value[left] > self.min_value[right]:
            self.min_value[k] = self.min_value[right]
            self.min_count[k] = self.min_count[right]
            self.second_min_value[k] = min(self.min_value[left], self.second_min_value[right])
        else:
            self.min_value[k] = self.min_value[left]
            self.min_count[k] = self.min_count[left] + self.min_count[right]
            self.second_min_value[k] = min(self.second_min_value[left], self.second_min_value[right])

    def _propagate(self, k: int):
        """Propagate pending updates to child nodes."""
        if self.tree_size <= k:  # If k is a leaf node
            return
        left, right = 2 * k, 2 * k + 1
        # Propagate set updates
        if self.pending_update[k] != self.POS_INF:
            self._apply_update(left, self.pending_update[k])
            self._apply_update(right, self.pending_update[k])
            self.pending_update[k] = self.POS_INF
            return
        # Propagate additions
        if self.pending_addition[k]:
            self._apply_add(left, self.pending_addition[k])
            self._apply_add(right, self.pending_addition[k])
            self.pending_addition[k] = 0
        # Propagate min and max constraints
        if self.max_value[left] > self.max_value[k]:
            self._apply_lower_clamping(left, self.max_value[k])
        if self.min_value[left] < self.min_value[k]:
            self._apply_upper_clamping(left, self.min_value[k])
        if self.max_value[right] > self.max_value[k]:
            self._apply_lower_clamping(right, self.max_value[k])
        if self.min_value[right] < self.min_value[k]:
            self._apply_upper_clamping(right, self.min_value[k])

    def _apply_update(self, k: int, x):
        """Set all elements in node k to x."""
        self.max_value[k] = self.min_value[k] = x
        self.second_max_value[k] = self.NEG_INF
        self.second_min_value[k] = self.POS_INF
        length = self.right_bound[k] - self.left_bound[k]
        self.max_count[k] = self.min_count[k] = length
        self.segment_sum[k] = x * length
        self.pending_addition[k] = 0
        self.pending_update[k] = x

    def _apply_add(self, k: int, x):
        """Add x to all elements in node k."""
        self.max_value[k] += x
        if self.second_max_value[k] != self.NEG_INF:
            self.second_max_value[k] += x
        self.min_value[k] += x
        if self.second_min_value[k] != self.POS_INF:
            self.second_min_value[k] += x
        length = self.right_bound[k] - self.left_bound[k]
        self.segment_sum[k] += x * length
        if self.pending_update[k] != self.POS_INF:
            self.pending_update[k] += x
        else:
            self.pending_addition[k] += x

    def _apply_lower_clamping(self, k: int, x):
        """Set elements in node k to min(x, current_value)."""
        if self.max_value[k] <= x:
            return
        delta = self.max_value[k] - x
        self.segment_sum[k] -= delta * self.max_count[k]
        self.max_value[k] = x
        if self.second_max_value[k] > x:
            self.second_max_value[k] = x
        if self.min_value[k] > x:
            self.min_value[k] = x
        if self.pending_update[k] != self.POS_INF and x < self.pending_update[k]:
            self.pending_update[k] = x

    def _apply_upper_clamping(self, k: int, x):
        """Set elements in node k to max(x, current_value)."""
        if self.min_value[k] >= x:
            return
        delta = x - self.min_value[k]
        self.segment_sum[k] += delta * self.min_count[k]
        self.min_value[k] = x
        if self.second_min_value[k] < x:
            self.second_min_value[k] = x
        if self.max_value[k] < x:
            self.max_value[k] = x
        if self.pending_update[k] != self.POS_INF and self.pending_update[k] < x:
            self.pending_update[k] = x

    def _apply_sqrt(self, k: int):
        """Set elements in node k to isqrt(x)."""
        if self.max_value[k] <= 1:
            return
        val = isqrt(self.max_value[k])
        length = self.right_bound[k] - self.left_bound[k]
        self.max_value[k] = self.min_value[k] = val  # Update min and max values
        self.segment_sum[k] = val * length  # Update the sum of the segment
        self.second_max_value[k] = self.NEG_INF  # Reset second max value
        self.second_min_value[k] = self.POS_INF  # Reset second min value
        self.max_count[k] = self.min_count[k] = length  # All elements are now equal
        self.pending_addition[k] = 0  # Clear any pending additions
        self.pending_update[k] = self.POS_INF  # Clear any pending updates

    def _range_operation(self, l: int, r: int, cmp1, cmp2, apply_func) -> None:
        """Generic method for applying operations over a range."""
        stack, order = [1], []
        while stack:
            k = stack.pop()
            if r <= self.left_bound[k] or self.right_bound[k] <= l or cmp1(k):
                continue
            if l <= self.left_bound[k] and self.right_bound[k] <= r and cmp2(k):
                apply_func(k)
                continue
            order.append(k)
            self._propagate(k)
            stack.extend([2 * k + 1, 2 * k])
        for v in reversed(order):
            self._merge(v)

    def range_lower_clamping(self, l: int, r: int, x: int) -> None:
        """Update elements in [l, r) to min(x, A[i])."""
        cmp1 = lambda k: self.max_value[k] <= x
        cmp2 = lambda k: self.second_max_value[k] < x
        apply_func = lambda k: self._apply_lower_clamping(k, x)
        self._range_operation(l, r, cmp1, cmp2, apply_func)

    def range_upper_clamping(self, l: int, r: int, x: int) -> None:
        """Update elements in [l, r) to max(x, A[i])."""
        cmp1 = lambda k: x <= self.min_value[k]
        cmp2 = lambda k: x < self.second_min_value[k]
        apply_func = lambda k: self._apply_upper_clamping(k, x)
        self._range_operation(l, r, cmp1, cmp2, apply_func)

    def range_add(self, l: int, r: int, x: int) -> None:
        """Add x to elements in [l, r)."""
        cmp1 = lambda _: False
        cmp2 = lambda _: True
        apply_func = lambda k: self._apply_add(k, x)
        self._range_operation(l, r, cmp1, cmp2, apply_func)

    def range_sqrt(self, l: int, r: int) -> None:
        """apply sqrt to elements in [l, r)."""
        cmp1 = lambda k: self.max_value[k] <= 1
        cmp2 = lambda k: int(self.max_value[k]**.5)-self.max_value[k] == int(self.min_value[k]**.5)-self.min_value[k]
        apply_func = lambda k: self._apply_add(k, int(self.max_value[k]**.5)-self.max_value[k])
        self._range_operation(l, r, cmp1, cmp2, apply_func)

    def range_update(self, l: int, r: int, x: int) -> None:
        """Set elements in [l, r) to x."""
        cmp1 = lambda _: False
        cmp2 = lambda _: True
        apply_func = lambda k: self._apply_update(k, x)
        self._range_operation(l, r, cmp1, cmp2, apply_func)

    def _range_query(self, l: int, r: int, initial_value, compare_func):
        """Generic method for querying over a range."""
        stack, res = [1], initial_value
        while stack:
            k = stack.pop()
            if r <= self.left_bound[k] or self.right_bound[k] <= l:
                continue
            if l <= self.left_bound[k] and self.right_bound[k] <= r:
                res = compare_func(res, k)
                continue
            self._propagate(k)
            stack.extend([2 * k + 1, 2 * k])
        return res

    def get_max(self, l: int, r: int):
        """Get the maximum value in [l, r)."""
        initial_value = self.NEG_INF
        compare_func = lambda v, k: max(v, self.max_value[k])
        return self._range_query(l, r, initial_value, compare_func)

    def get_min(self, l: int, r: int):
        """Get the minimum value in [l, r)."""
        initial_value = self.POS_INF
        compare_func = lambda v, k: min(v, self.min_value[k])
        return self._range_query(l, r, initial_value, compare_func)

    def get_sum(self, l: int, r: int):
        """Get the sum of elements in [l, r)."""
        initial_value = 0
        compare_func = lambda v, k: v + self.segment_sum[k]
        return self._range_query(l, r, initial_value, compare_func)

    def __getitem__(self, i):
        if i < -self.n or self.n <= i:
            raise IndexError(f"Index out of range: {i}")
        if i < 0:
            i += self.n
        return self.get_sum(i, i + 1)

    def __setitem__(self, i, val):
        if i < -self.n or self.n <= i:
            raise IndexError(f"Index out of range: {i}")
        if i < 0:
            i += self.n
        self.range_update(i, i + 1, val)

    def __iter__(self):
        yield from (self.get_sum(i, i + 1) for i in range(self.n))

    def __str__(self):
        return str(list(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({list(self)})"


def print_attributes(obj):
    result = []
    class_name = obj.__class__.__name__
    result.append(f"Class: {class_name}")

    attributes = dir(obj)

    for attribute in attributes:
        if not attribute.startswith("__"):
            attr_value = getattr(obj, attribute)
            result.append(f"{attribute}: {attr_value!r}")
    return result


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_009
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        stb = SegmentTreeBeats(n, [int(input()) for _ in range(n)])
        m = int(input())
        for _ in range(m):
            q = int(input())
            if q == 1:
                l, r, x = (int(input()) for _ in range(3))
                stb.range_add(l - 1, r, x)
            if q == 2:
                l, r = (int(input()) for _ in range(2))
                stb.range_sqrt(l - 1, r)
            if q == 3:
                l, r = (int(input()) for _ in range(2))
                answer = stb.get_sum(l - 1, r)
                answers.append(f"{answer}")
print(*answers, sep="\n")