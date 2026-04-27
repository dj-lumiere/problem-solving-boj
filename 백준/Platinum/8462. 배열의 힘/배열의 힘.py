# 14897 서로 다른 수와 쿼리 1
from collections import Counter
from sys import stdin


def input():
    return stdin.readline().strip()

def main():
    N, Q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    # print(A)
    queries = [tuple(map(lambda x: x - 1, map(int, input().split()))) for _ in range(Q)]
    query_order = {v: [] for v in queries}
    for i, (s, e) in enumerate(queries):
        query_order[(s, e)].append(i)
    bucket_size = int(N**0.5) + 1
    queries.sort(key=lambda x: (x[0] // bucket_size, x[1]))
    current_counter = [0 for _ in range(10**6+1)]
    current_answer = 0
    answer = [0 for _ in range(Q)]
    last_query = [0, 0]
    for i, (s, e) in enumerate(queries):
        if i == 0:
            for j in range(s, e + 1):
                current_counter[A[j]] += 1
                current_answer += (current_counter[A[j]]*2-1)*A[j]
            for j in query_order[(s, e)]:
                answer[j] = current_answer
            last_query = [s, e]
            continue
        s_before, e_before = last_query
        if s_before > s:
            for j in range(s, s_before):
                current_counter[A[j]] += 1
                current_answer += (current_counter[A[j]]*2-1)*A[j]
        elif s_before < s:
            for j in range(s_before, s):
                current_counter[A[j]] -= 1
                current_answer -= (current_counter[A[j]]*2+1)*A[j]
        if e_before > e:
            for j in range(e + 1, e_before + 1):
                current_counter[A[j]] -= 1
                current_answer -= (current_counter[A[j]]*2+1)*A[j]
        elif e_before < e:
            for j in range(e_before + 1, e + 1):
                current_counter[A[j]] += 1
                current_answer += (current_counter[A[j]]*2-1)*A[j]
        # print(s, e, current_counter[:10], current_answer, answer)
        for j in query_order[(s, e)]:
            answer[j] = current_answer
        last_query = [s, e]
    print(*answer, sep="\n")

main()
2