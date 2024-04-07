import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = int(input())
        n_over_i = []
        for j in range(1, int(n ** .5) + 1):
            a, b = j, n // j
            n_over_i.extend([j, n // j])
        n_over_i = sorted(set(n_over_i), reverse=True)
        n_over_i_interval = list(reversed(n_over_i))
        answer = 0
        for j, (v1, v2) in enumerate(zip(n_over_i, n_over_i_interval)):
            if j == 0:
                answer += v1 * v2
                continue
            start = n_over_i_interval[j - 1] + 1
            end = v2
            answer += v1 * (start + end) * (end - start + 1) // 2
        answers[i] = f"{answer}"
    print(answers)