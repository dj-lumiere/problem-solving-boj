# 30039 Queueueue

from collections import deque
from sys import stdin


def input():
    return stdin.readline().strip()


class Queueueue:
    def __init__(self):
        self.center = 0
        self.left: deque[int] = deque()
        self.right: deque[int] = deque()
        self.up: deque[int] = deque()
        self.down: deque[int] = deque()
        self.horizontal_size = 0
        self.vertical_size = 0

    def hpush(self, x):
        if not self.center:
            self.center = x
        else:
            self.right.append(x)
            self.horizontal_size += 1
        if len(self.left) + 1 < len(self.right):
            self.left.append(self.center)
            self.center = self.right.popleft()

    def hpop(self):
        result = -1
        if not self.center:
            return -1
        elif not self.horizontal_size and not self.vertical_size:
            result = self.center
            self.center = 0
        elif not self.horizontal_size and self.vertical_size:
            result = self.center
            self.vertical_size -= 1
            if len(self.up) < len(self.down):
                self.center = self.down.popleft()
            else:
                self.center = self.up.pop()
        elif not self.left:
            result = self.center
            self.center = self.right.popleft()
            self.horizontal_size -= 1
        else:
            result = self.left.popleft()
            self.horizontal_size -= 1
            if len(self.left) + 1 < len(self.right):
                self.left.append(self.center)
                self.center = self.right.popleft()
        return result

    def hfront(self):
        if not self.left and not self.center and not self.right:
            return -1
        if not self.left:
            return self.center
        return self.left[0]

    def hback(self):
        if not self.left and not self.center and not self.right:
            return -1
        if not self.right:
            return self.center
        return self.right[-1]

    def hsize(self):
        return self.horizontal_size + (1 if self.center else 0)

    def vpush(self, x):
        if not self.center:
            self.center = x
        else:
            self.down.append(x)
            self.vertical_size += 1
        if len(self.up) + 1 < len(self.down):
            self.up.append(self.center)
            self.center = self.down.popleft()

    def vpop(self):
        result = -1
        if not self.center:
            return -1
        elif not self.vertical_size and not self.horizontal_size:
            result = self.center
            self.center = 0
        elif not self.vertical_size and self.horizontal_size:
            result = self.center
            self.horizontal_size -= 1
            if len(self.left) < len(self.right):
                self.center = self.right.popleft()
            else:
                self.center = self.left.pop()
        elif not self.up:
            result = self.center
            self.center = self.down.popleft()
            self.vertical_size -= 1
        else:
            result = self.up.popleft()
            self.vertical_size -= 1
            if len(self.up) + 1 < len(self.down):
                self.up.append(self.center)
                self.center = self.down.popleft()
        return result

    def vfront(self):
        if not self.up and not self.center and not self.down:
            return -1
        if not self.up:
            return self.center
        return self.up[0]

    def vback(self):
        if not self.up and not self.center and not self.down:
            return -1
        if not self.down:
            return self.center
        return self.down[-1]

    def vsize(self):
        return self.vertical_size + (1 if self.center else 0)

    def size(self):
        return self.horizontal_size + self.vertical_size + (1 if self.center else 0)

    def empty(self):
        return 0 if self.size() else 1

    def middle(self):
        if not self.center:
            return -1
        return self.center

    def __str__(self) -> str:
        return f"{self.horizontal_size=} {self.vertical_size=}\n{self.up}\n{self.left} {self.center} {self.right}\n{self.down}"


my_queueueue = Queueueue()
N = int(input())
for _ in range(N):
    command, *parameter = input().split(" ")
    if command == "hpush":
        my_queueueue.hpush(int(parameter[0]))
        continue
    if command == "vpush":
        my_queueueue.vpush(int(parameter[0]))
        continue
    result = None
    if command == "hpop":
        result = my_queueueue.hpop()
    if command == "hfront":
        result = my_queueueue.hfront()
    if command == "hback":
        result = my_queueueue.hback()
    if command == "hsize":
        result = my_queueueue.hsize()
    if command == "vpop":
        result = my_queueueue.vpop()
    if command == "vfront":
        result = my_queueueue.vfront()
    if command == "vback":
        result = my_queueueue.vback()
    if command == "vsize":
        result = my_queueueue.vsize()
    if command == "size":
        result = my_queueueue.size()
    if command == "empty":
        result = my_queueueue.empty()
    if command == "middle":
        result = my_queueueue.middle()
    print(f"{result}")