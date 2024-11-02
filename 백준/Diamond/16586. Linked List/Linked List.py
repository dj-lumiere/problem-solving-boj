from sys import stderr, stdout


class Node:
    __slots__ = ('left', 'right', 'parent', 'size', 'key', 'rev')

    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.size = 0
        self.key = 0
        self.rev = False

    def reset(self):
        self.left = None
        self.right = None
        self.parent = None
        self.size = 0
        self.key = 0
        self.rev = False

    def __repr__(self):
        return (f"Node(key={self.key}, size={self.size}, rev={self.rev})")


class SplayTree:
    def __init__(self):
        self.root = None  # Index of the root node in self.tree
        self.tree = [Node() for _ in range(100002)]  # List of Node instances

    def clear(self):
        self.root = None
        for i in range(100002):
            self.tree[i].reset()

    def build_tree(self, n, keys):
        for i in range(n + 2):
            self.tree[i].reset()
        self.root = self.tree[0]
        self.root.key = 0
        last = self.root
        for v in keys:
            current = self.tree[v]
            current.parent = last
            current.key = v
            last.right = current
            last = last.right
        last.right = self.tree[n + 1]
        last.right.key = 10 ** 9
        last.right.parent = last
        for i in reversed(range(n + 2)):
            self.update(self.tree[i])

    def __repr__(self, level=0, pos=None):
        if pos is None:
            pos = self.root  # Set pos to self.root if no value is passed

        if pos is None:
            return ""
        indent = "    " * level
        left_string = (
            f"    {indent}L{level + 1}={self.__repr__(level=level + 1, pos=pos.left)}"
            if pos.left is not None
            else ""
        )
        right_string = (
            f"    {indent}R{level + 1}={self.__repr__(level=level + 1, pos=pos.right)}"
            if pos.right is not None
            else ""
        )
        return (f"{self.tree}\nroot=" if level == 0 else "") + f"{pos!r}" + (
            f"\n{left_string}" if pos.left is not None else "") + (
            f"\n{right_string}" if pos.right is not None else "")

    def __getitem__(self, item):
        st.kth_to_root(item)
        return self.root.key

    def __iter__(self):
        return iter([st[i] for i in range(1, len(self.tree) - 1)])

    def update(self, x):
        x.size = 1
        if x.left:
            x.size += x.left.size
        if x.right:
            x.size += x.right.size

    def push_down(self, x):
        if not x.rev:
            return
        x.left, x.right = x.right, x.left
        x.rev = False
        if x.left: x.left.rev = not x.left.rev
        if x.right: x.right.rev = not x.right.rev

    def rotate(self, x):
        parent = x.parent
        b = None
        self.push_down(parent)
        self.push_down(x)
        if x == parent.left:
            parent.left = b = x.right
            x.right = parent
        else:
            parent.right = b = x.left
            x.left = parent
        x.parent = parent.parent
        parent.parent = x
        if b: b.parent = parent
        if x.parent:
            if parent == x.parent.left:
                x.parent.left = x
            else:
                x.parent.right = x
        else:
            self.root = x
        self.update(parent)
        self.update(x)

    def splay(self, x, g=None):
        while x.parent != g:
            parent = x.parent
            if parent.parent == g:
                self.rotate(x)
                break
            pp = parent.parent
            if (parent.left == x) == (pp.left == parent):
                self.rotate(parent)
                self.rotate(x)
            else:
                self.rotate(x)
                self.rotate(x)
        if not g:
            self.root = x

    def kth_to_root(self, k):
        x = self.root
        self.push_down(x)
        while True:
            while x.left and x.left.size > k:
                x = x.left
                self.push_down(x)
            if x.left:
                k -= x.left.size
            if not k:
                break
            k -= 1
            x = x.right
            self.push_down(x)
        self.splay(x)

    def isolate_range(self, l, r):
        self.kth_to_root(r + 1)
        tmp = self.root
        self.kth_to_root(l - 1)
        self.splay(tmp, self.root)
        return self.root.right.left

    def query(self, l, r):
        self.isolate_range(l, r)
        node = self.root.right.left
        return node.min, node.max, node.sum

    def reverse_range(self, l, r):
        self.isolate_range(l, r)
        x = self.root.right.left
        x.rev = not x.rev

    def shift(self, l, r, c):
        k = r - l + 1
        c %= k
        if c > 0:
            self.reverse_range(l, r)
            self.reverse_range(l + c, r)
            self.reverse_range(l, l + c - 1)

    def shift_single(self, l, c):
        if c > 0:
            self.reverse_range(l, l + c)
            self.reverse_range(l, l + c - 1)
        elif c < 0:
            self.reverse_range(l + c, l)
            self.reverse_range(l + c + 1, l)

    def index(self, x):
        self.splay(self.tree[x])
        return self.root.left.size

    def slide(self, x, y):
        x_idx = self.index(x)
        y_idx = self.index(y)
        shift = y_idx - x_idx
        if shift < 0:
            shift += 1
        self.shift_single(x_idx, shift)
        return shift


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    answers = []
    INF = 10 ** 18
    t = 1
    st = SplayTree()
    for hh in range(t):
        n = int(input())
        q = int(input())
        st.build_tree(n, range(1, n + 1))
        for i in range(q):
            x, y = int(input()), int(input())
            answer = st.slide(x, y)
            answers.append(answer)
        answers.append(" ".join(map(str, [st[i] for i in range(1, n + 1)])))
    print(*answers, sep="\n")