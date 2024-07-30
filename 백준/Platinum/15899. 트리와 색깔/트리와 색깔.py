from sys import stdin
from math import log2, ceil
from random import shuffle
from bisect import bisect_right
from os import write


class SegmentTree:
    """This class is for faster range queries and updates on a list.
    This class gets a list called "members" and does the tree building process in a seperate array called "tree".
    Then, it does the query and update in fittingly named function called "query" and "updates", respectively.
    Keep in mind that when calling "query" and "update", the index uses "ZERO BASED NUMBERING" system.
    """

    def __init__(self, members):
        # 어차피 필요한 멤버 갯수 빼고는 0으로 패딩 예정이라 깔끔하게 2의 승수가 될 수 있게 설정함
        self.member_count = len(members)
        self.tree_max_level = ceil(log2(self.member_count))
        self.tree_capacity = 1 << self.tree_max_level
        self.tree = [[] for _ in range(self.tree_capacity << 1)]
        self.build(members)

    def build(self, members):
        for index, member in enumerate(members):
            self.tree[self.tree_capacity + index].extend(member)
        for i in range(self.tree_capacity - 1, 0, -1):
            self.tree[i] = self.merge(self.tree[2 * i + 0],self.tree[2 * i + 1])

    def merge(self, target1, target2):
        result = []
        target11 = target1[:]
        target21 = target2[:]
        while target11 and target21:
            i = target11.pop()
            j = target21.pop()
            if i >= j:
                result.append(i)
                target21.append(j)
            else:
                result.append(j)
                target11.append(i)
        result.extend(target11[::-1])
        result.extend(target21[::-1])
        result.reverse()
        return result

    def query(self, index_start, index_end, k):
        index_start += self.tree_capacity - 1
        index_end += self.tree_capacity - 1
        result = 0
        while index_start <= index_end:
            if index_start % 2 == 1:
                result += bisect_right(self.tree[index_start], k)
                index_start += 1
            if index_end % 2 == 0:
                result += bisect_right(self.tree[index_end], k)
                index_end -= 1
            index_start >>= 1
            index_end >>= 1
        return result

    def __str__(self) -> str:
        dfs_stack = [(0, 1)]
        result = []
        while dfs_stack:
            level, pos = dfs_stack.pop()
            if pos >= self.tree_capacity * 2:
                continue
            indent = "    " * level
            if level == self.tree_max_level:
                member_index = pos - self.tree_capacity
                result.append(
                    f"{indent}member{member_index+1}[index={pos}]={self.tree[pos]}"
                )
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


def dfs(root, graph, size):
    time = 0
    stack = [(root, False)]
    time_in = [0] * (size + 1)
    time_out = [0] * (size + 1)
    while stack:
        node, visited = stack.pop()
        if not visited:
            time += 1
            time_in[node] = time
            stack.append((node, True))
            for child in graph[node]:
                if time_in[child] == 0:
                    stack.append((child, False))
        else:
            time_out[node] = time
    return time_in, time_out


with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    n = int(input())
    t = int(input())
    c = int(input())
    color = [0] + [int(input()) for _ in range(n)]
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        s, e = int(input()), int(input())
        graph[s].append(e)
        graph[e].append(s)
    time_in, time_out = dfs(root=1, graph=graph, size=n)
    a = [0 for _ in range(n+1)]
    for i, v in enumerate(time_in):
        a[v] = color[i]
    my_tree = SegmentTree([[i] for i in a[1:]])
    answer = 0
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    for hh in range(t):
        i, j = [int(input()) for _ in range(2)]
        start = time_in[i]
        end = time_out[i]
        answer += my_tree.query(start, end, j)
        answer %= 1000000007
    answers.append(f"{answer}")
    print(answers)