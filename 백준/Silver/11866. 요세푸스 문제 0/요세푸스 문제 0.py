# 11866 요세푸스 문제 0

from collections import deque


class CircularDeque:
    def __init__(self, member_count: int) -> None:
        self.value = deque([i for i in range(1, member_count + 1)])

    def remove_kth(self, k: int) -> list[int]:
        result = []
        while self.value:
            for _ in range(k - 1):
                self.value.append(self.value.popleft())
            result.append(self.value.popleft())
        return result


N, K = (int(i) for i in input().split(" "))
my_circular_deque = CircularDeque(N)
print("<", end="")
print(*my_circular_deque.remove_kth(K), sep=", ", end=">")