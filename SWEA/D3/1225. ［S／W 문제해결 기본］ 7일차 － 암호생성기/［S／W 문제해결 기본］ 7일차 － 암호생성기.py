from collections import deque

answers = []
INF = 10 ** 18
t = 10
DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for hh in range(t):
    _ = int(input())
    numbers = list(map(int, input().split()))
    minimum_cycles = max(min(i // 15 for i in numbers)-1, 0)
    numbers = [i - minimum_cycles * 15 for i in numbers]
    not_finished = True
    current_number = 1
    queue = deque(numbers)
    while not_finished:
        target = queue.popleft()
        if target - current_number <= 0:
            queue.append(0)
            not_finished = False
            break
        queue.append(target - current_number)
        current_number += 1
        if current_number > 5:
            current_number -= 5
    answer = " ".join(map(str, queue))
    answers.append(f"#{hh + 1} {answer}")
print(*answers, sep="\n")
