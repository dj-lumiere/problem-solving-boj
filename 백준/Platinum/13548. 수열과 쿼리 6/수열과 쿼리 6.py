# 13548 수열과 쿼리 6
from collections import Counter
from sys import stdin


def input():
    return stdin.readline().strip()


def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [tuple(map(lambda x: x - 1, map(int, input().split()))) for _ in range(Q)]
    query_order = {v: [] for v in queries}
    for i, (s, e) in enumerate(queries):
        query_order[(s, e)].append(i)
    bucket_size = int(N**0.5) + 1
    queries.sort(key=lambda x: (x[0] // bucket_size, x[1]))
    current_counter = [0 for _ in range(100001)]
    frequency_counter = [0 for _ in range(N + 1)]
    frequency_counter[0] = N
    current_max_freq = 0
    answer = [0 for _ in range(Q)]
    last_query = [0, 0]
    for i, (s, e) in enumerate(queries):
        if i == 0:
            for j in range(s, e + 1):
                frequency_counter[current_counter[A[j]]] -= 1
                frequency_counter[current_counter[A[j]] + 1] += 1
                current_counter[A[j]] += 1
                if frequency_counter[current_max_freq + 1] == 1:
                    current_max_freq += 1
            for j in query_order[(s, e)]:
                answer[j] = current_max_freq
            last_query = [s, e]
            continue
        s_before, e_before = last_query
        if s_before > s:
            for j in range(s, s_before):
                frequency_counter[current_counter[A[j]]] -= 1
                frequency_counter[current_counter[A[j]] + 1] += 1
                current_counter[A[j]] += 1
                if frequency_counter[current_max_freq + 1] == 1:
                    current_max_freq += 1
        elif s_before < s:
            for j in range(s_before, s):
                frequency_counter[current_counter[A[j]]] -= 1
                frequency_counter[current_counter[A[j]] - 1] += 1
                current_counter[A[j]] -= 1
                if frequency_counter[current_max_freq] == 0:
                    current_max_freq -= 1
        if e_before > e:
            for j in range(e + 1, e_before + 1):
                frequency_counter[current_counter[A[j]]] -= 1
                frequency_counter[current_counter[A[j]] - 1] += 1
                current_counter[A[j]] -= 1
                if frequency_counter[current_max_freq] == 0:
                    current_max_freq -= 1
        elif e_before < e:
            for j in range(e_before + 1, e + 1):
                frequency_counter[current_counter[A[j]]] -= 1
                frequency_counter[current_counter[A[j]] + 1] += 1
                current_counter[A[j]] += 1
                if frequency_counter[current_max_freq + 1] == 1:
                    current_max_freq += 1
        for j in query_order[(s, e)]:
            answer[j] = current_max_freq
        last_query = [s, e]
    print(*answer, sep="\n")


main()