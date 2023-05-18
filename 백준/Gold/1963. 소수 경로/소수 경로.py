# 1963 소수 경로
from math import ceil
from collections import deque

# 일단 소수들 전부 다 구하기
prime_checker: list[bool] = [True for _ in range(10000)]
prime_checker[0] = False
prime_checker[1] = False
for i in range(100):
    if prime_checker[i] == True:
        prime_checker[i::i] = [False] * (ceil(10000 / i) - 1)
        prime_checker[i] = True
prime_checker[:1000] = [False] * 1000
# bfs를 통해 소수들을 전부 다 구해보기는 하지만, 만약 어느순간 도달이 불가능해진다면 바로 "Impossible" 출력
T = int(input())
for _ in range(T):
    a, b = list(map(int, input().split(" ")))
    visited = [not j for i, j in enumerate(prime_checker)]
    bfs_deque = deque()
    bfs_deque.append((0, a))
    result = -1
    while bfs_deque:
        path_len, next_number = bfs_deque.popleft()
        visited[next_number] = True
        if next_number == b:
            result = path_len
            bfs_deque.clear()
            break
        else:
            adding_queue = 0
            for i in range(10):
                first_digit_change = (
                    next_number // 10000 * 10000 + i * 1000 + next_number % 1000
                )
                second_digit_change = (
                    next_number // 1000 * 1000 + i * 100 + next_number % 100
                )
                third_digit_change = (
                    next_number // 100 * 100 + i * 10 + next_number % 10
                )
                fourth_digit_change = next_number // 10 * 10 + i * 1 + next_number % 1
                if not visited[first_digit_change] and first_digit_change != next_number:
                    visited[first_digit_change] = True
                    bfs_deque.append((path_len+1, first_digit_change))
                    adding_queue += 1
                if not visited[second_digit_change] and second_digit_change != next_number:
                    visited[second_digit_change] = True
                    bfs_deque.append((path_len+1, second_digit_change))
                    adding_queue += 1
                if not visited[third_digit_change] and third_digit_change != next_number:
                    visited[third_digit_change] = True
                    bfs_deque.append((path_len+1, third_digit_change))
                    adding_queue += 1
                if not visited[fourth_digit_change] and fourth_digit_change != next_number:
                    visited[fourth_digit_change] = True
                    bfs_deque.append((path_len+1, fourth_digit_change))
                    adding_queue += 1
    if result == -1:
        print("Impossible")
    else:
        print(result)