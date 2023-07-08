# 1021 회전하는 큐
from typing import Optional


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

    def rotate_left(self) -> int:
        if self.length != 0:
            self.push_right(self.pop_left())
        return -1

    def rotate_right(self) -> int:
        if self.length != 0:
            self.push_left(self.pop_right())
        return -1

    def len(self) -> int:
        return self.length

    def __len__(self) -> int:
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

    def __getitem__(self, b):
        if b < 0:
            b += self.length
        if b > self.length:
            raise KeyError
        return self.val[self.deque_left_ptr + b]

    def index(self, b: int) -> Optional[int]:
        return self.val[self.deque_left_ptr : self.deque_right_ptr + 1].index(b)


N, M = map(int, input().split(" "))
my_list_deque = ListDeque()
for i in range(1, N + 1):
    my_list_deque.push_right(i)
operation2_count, operation3_count = 0, 0
X = list(map(int, input().split(" ")))
for i in X:
    i_pos = my_list_deque.index(i)
    if i_pos > len(my_list_deque) - i_pos:
        for _ in range(len(my_list_deque) - i_pos):
            my_list_deque.rotate_right()
            operation3_count += 1
        my_list_deque.pop_left()
    else:
        for _ in range(i_pos):
            my_list_deque.rotate_left()
            operation2_count += 1
        my_list_deque.pop_left()
print(operation2_count + operation3_count)