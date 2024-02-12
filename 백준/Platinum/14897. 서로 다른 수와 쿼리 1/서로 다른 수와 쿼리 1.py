# 14897 서로 다른 수와 쿼리 1

import os
from array import array


def main():
    tokens = iter(os.read(0, os.fstat(0).st_size).split())
    N = int(next(tokens))
    A = array("I", [int(next(tokens)) for _ in range(N)])
    A_order = {v: i for i, v in enumerate(sorted(set(A)))}
    for i, v in enumerate(A):
        A[i] = A_order[v]
    # print(A)
    Q = int(next(tokens))
    queries = [(int(next(tokens)) - 1, int(next(tokens)) - 1) for _ in range(Q)]
    query_order = {v: [] for v in queries}
    for i, (s, e) in enumerate(queries):
        query_order[(s, e)].append(i)
    bucket_size = int(N**0.5) + 1
    queries.sort(key=lambda x: (x[0] // bucket_size, x[1]))
    current_counter = array("i", [0 for _ in range(N)])
    current_length = 0
    answer = array("i", [0 for _ in range(Q)])
    last_query = [0, 0]
    for i, (s, e) in enumerate(queries):
        if i == 0:
            for j in range(s, e + 1):
                current_counter[A[j]] += 1
                if current_counter[A[j]] == 1:
                    current_length += 1
            for j in query_order[(s, e)]:
                answer[j] = current_length
            last_query = [s, e]
            continue
        s_before, e_before = last_query
        if s_before > s:
            for j in range(s, s_before):
                current_counter[A[j]] += 1
                if current_counter[A[j]] == 1:
                    current_length += 1
        elif s_before < s:
            for j in range(s_before, s):
                current_counter[A[j]] -= 1
                if current_counter[A[j]] == 0:
                    current_length -= 1
        if e_before > e:
            for j in range(e + 1, e_before + 1):
                current_counter[A[j]] -= 1
                if current_counter[A[j]] == 0:
                    current_length -= 1
        elif e_before < e:
            for j in range(e_before + 1, e + 1):
                current_counter[A[j]] += 1
                if current_counter[A[j]] == 1:
                    current_length += 1
        # print(s, e, current_counter, current_length, answer)
        for j in query_order[(s, e)]:
            answer[j] = current_length
        last_query = [s, e]
    os.write(1, "\n".join(map(str, answer)).encode())


main()