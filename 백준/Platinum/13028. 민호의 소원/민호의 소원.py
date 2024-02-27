# 13028 민호의 소원

import os
from array import array


def main():
    tokens = iter(os.read(0, os.fstat(0).st_size).split())
    N = int(next(tokens))
    Q = int(next(tokens))
    A = array("I", [int(next(tokens)) for _ in range(N)])
    A_order = {v: i for i, v in enumerate(sorted(set(A)))}
    for i, v in enumerate(A):
        A[i] = A_order[v]
    queries = [(int(next(tokens)) - 1, int(next(tokens)) - 1, i) for i in range(Q)]
    bucket_size = int(N ** 0.5) + 1
    queries.sort(key=lambda x: (x[0] // bucket_size, x[1]))
    current_counter = array("i", [0 for _ in range(N)])
    frequency_counter = array("i", [0 for _ in range(N + 1)])
    frequency_counter[0] = N
    answer = ["" for _ in range(Q)]
    last_query = [0, 0]
    for i, (s, e, k) in enumerate(queries):
        if i == 0:
            for j in range(s, e + 1):
                frequency_counter[current_counter[A[j]] + 1] += 1
                current_counter[A[j]] += 1
            answer[k] = str(frequency_counter[3])
            last_query = [s, e]
            continue
        s_before, e_before = last_query
        if s_before > s:
            for j in range(s, s_before):
                frequency_counter[current_counter[A[j]] + 1] += 1
                current_counter[A[j]] += 1
        elif s_before < s:
            for j in range(s_before, s):
                frequency_counter[current_counter[A[j]]] -= 1
                current_counter[A[j]] -= 1
        if e_before > e:
            for j in range(e + 1, e_before + 1):
                frequency_counter[current_counter[A[j]]] -= 1
                current_counter[A[j]] -= 1
        elif e_before < e:
            for j in range(e_before + 1, e + 1):
                frequency_counter[current_counter[A[j]] + 1] += 1
                current_counter[A[j]] += 1
        answer[k] = str(frequency_counter[3])
        last_query = [s, e]
    os.write(1, "\n".join(answer).encode())
    os._exit(0)


main()