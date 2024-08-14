from sys import stdout, stderr


class ListNode:
    def __init__(self, current=None, prev=None, next=None):
        self.current = current
        self.prev = prev
        self.next = next

    def __str__(self):
        if self.next is None:
            return self.current
        return self.current + "" + str(self.next)

    def __repr__(self):
        return f"ListNode[current={self.current}, prev={self.prev}, next={self.next}"


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = int(input())
    answers = []
    for hh in range(t):
        s = input()
        password_start = ListNode("")
        current_cursor = password_start
        cursor = 0
        length = 0
        for i, v in enumerate(s):
            if v == "<":
                if current_cursor.prev is not None:
                    current_cursor = current_cursor.prev
            elif v == ">":
                if current_cursor.next is not None:
                    current_cursor = current_cursor.next
            elif v == "-":
                if current_cursor.prev is not None:
                    current_cursor.prev.next = current_cursor.next
                    if current_cursor.next is not None:
                        current_cursor.next.prev = current_cursor.prev
                    current_cursor = current_cursor.prev
                    length -= 1
            else:
                new_node = ListNode(v, prev=current_cursor)
                if current_cursor.next is not None:
                    new_node.next = current_cursor.next
                    current_cursor.next.prev = new_node
                current_cursor.next = new_node
                current_cursor = new_node
                length += 1
        result = []
        for _ in range(length + 1):
            result.append(password_start.current)
            password_start = password_start.next
        answer = "".join(result)
        answers.append(f"{answer}")
    print(*answers, sep="\n")
