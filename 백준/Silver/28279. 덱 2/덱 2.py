# 28279 덱 2

from sys import stdin, stdout

input = stdin.readline
print = stdout.write


class ListDeque:
    def __init__(self):
        self.val = [-1] * 2000001
        self.deque_left_ptr = 1000000
        self.deque_right_ptr = 999999
        self.length = 0

    def __str__(self):
        result = "> "
        for i in range(self.deque_left_ptr, self.deque_right_ptr + 1, 1):
            result += str(self.val[i]) + " "
        return f"{result}<"

    def push_left(self, X: int):
        self.val[self.deque_left_ptr - 1] = X
        self.deque_left_ptr -= 1
        self.length += 1

    def push_right(self, X: int):
        self.val[self.deque_right_ptr + 1] = X
        self.deque_right_ptr += 1
        self.length += 1

    def pop_left(self) -> int:
        if self.length != 0:
            self.deque_left_ptr += 1
            self.length -= 1
            return self.val[self.deque_left_ptr - 1]
        return -1

    def pop_right(self) -> int:
        if self.length != 0:
            self.deque_right_ptr -= 1
            self.length -= 1
            return self.val[self.deque_right_ptr + 1]
        return -1

    def len(self) -> int:
        return self.length

    def is_empty(self) -> int:
        if self.length == 0:
            return 1
        return 0

    def return_left(self) -> int:
        if self.length == 0:
            return -1
        return self.val[self.deque_left_ptr]

    def return_right(self) -> int:
        if self.length == 0:
            return -1
        return self.val[self.deque_right_ptr]


N = int(stdin.readline())
deque: ListDeque = ListDeque()
for _ in range(N):
    opcode, *operand = map(int, input().rstrip().split(" "))
    if opcode == 1:
        deque.push_left(operand[0])
    elif opcode == 2:
        deque.push_right(operand[0])
    elif opcode == 3:
        print(f"{deque.pop_left()}\n")
    elif opcode == 4:
        print(f"{deque.pop_right()}\n")
    elif opcode == 5:
        print(f"{deque.len()}\n")
    elif opcode == 6:
        print(f"{deque.is_empty()}\n")
    elif opcode == 7:
        print(f"{deque.return_left()}\n")
    elif opcode == 8:
        print(f"{deque.return_right()}\n")