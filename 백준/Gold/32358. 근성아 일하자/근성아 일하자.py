from bisect import bisect_left, bisect_right
from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdout, stderr

getcontext().prec = 30


"""from https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/SortedList.py"""
class FenwickTree:
    def __init__(self, x):
        bit = self.bit = list(x)
        size = self.size = len(bit)
        for i in range(size):
            j = i | (i + 1)
            if j < size:
                bit[j] += bit[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < self.size:
            self.bit[idx] += x
            idx |= idx + 1

    def __call__(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def find_kth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(self.size.bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < self.size and self.bit[right_idx] <= k:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1, k


class SortedList:
    block_size = 700

    def __init__(self, iterable=()):
        self.macro = []
        self.micros = [[]]
        self.micro_size = [0]
        self.fenwick = FenwickTree([0])
        self.size = 0
        for item in iterable:
            self.insert(item)

    def insert(self, x):
        i = bisect_left(self.macro, x)
        j = bisect_right(self.micros[i], x)
        self.micros[i].insert(j, x)
        self.size += 1
        self.micro_size[i] += 1
        self.fenwick.update(i, 1)
        if len(self.micros[i]) >= self.block_size:
            self.micros[i:i + 1] = self.micros[i][:self.block_size >> 1], self.micros[i][self.block_size >> 1:]
            self.micro_size[i:i + 1] = self.block_size >> 1, self.block_size >> 1
            self.fenwick = FenwickTree(self.micro_size)
            self.macro.insert(i, self.micros[i + 1][0])

    def pop(self, k=-1):
        i, j = self._find_kth(k)
        self.size -= 1
        self.micro_size[i] -= 1
        self.fenwick.update(i, -1)
        return self.micros[i].pop(j)

    def __getitem__(self, k):
        i, j = self._find_kth(k)
        return self.micros[i][j]

    def count(self, x):
        return self.upper_bound(x) - self.lower_bound(x)

    def __contains__(self, x):
        return self.count(x) > 0

    def lower_bound(self, x):
        i = bisect_left(self.macro, x)
        return self.fenwick(i) + bisect_left(self.micros[i], x)

    def upper_bound(self, x):
        i = bisect_right(self.macro, x)
        return self.fenwick(i) + bisect_right(self.micros[i], x)

    def _find_kth(self, k):
        return self.fenwick.find_kth(k + self.size if k < 0 else k)

    def __len__(self):
        return self.size

    def __iter__(self):
        return (x for micro in self.micros for x in micro)

    def __repr__(self):
        return str(list(self))


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        answer = 0
        current_tree_queue = SortedList()
        current_tree_queue.insert(-INF)
        current_tree_queue.insert(INF)
        current_position = 0
        for _ in range(n):
            c = int(input())
            if c == 1:
                d = int(input())
                current_tree_queue.insert(d)
            elif c == 2:
                while len(current_tree_queue) > 2:
                    if len(current_tree_queue) == 2:
                        break
                    my_pick1 = current_tree_queue[current_tree_queue.lower_bound(current_position) - 1]
                    my_pick2 = current_tree_queue[current_tree_queue.lower_bound(current_position)]
                    my_pick3 = current_tree_queue[min(len(current_tree_queue)-1,current_tree_queue.lower_bound(current_position) + 1)]
                    min_index = sorted([my_pick1, my_pick2, my_pick3], key=lambda x: (abs(x - current_position), x))[0]
                    #eprint(current_position, min_index, [my_pick1, my_pick2, my_pick3], current_tree_queue)
                    answer += abs(current_position - min_index)
                    current_position = min_index
                    current_tree_queue.pop(current_tree_queue.lower_bound(current_position))
                    #eprint(current_position, current_tree_queue, len(current_tree_queue))
                    if len(current_tree_queue) == 2:
                        break
        answers.append(f"{answer}")
    print(*answers, sep="\n")