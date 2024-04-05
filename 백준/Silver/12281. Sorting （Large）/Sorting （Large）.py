import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    for x in range(t):
        n = int(input())
        a = [int(input()) for _ in range(n)]
        a_odd = [v for i, v in enumerate(a) if v % 2 == 1]
        a_odd_index = [i for i, v in enumerate(a) if v % 2 == 1]
        a_even = [v for i, v in enumerate(a) if v % 2 == 0]
        a_even_index = [i for i, v in enumerate(a) if v % 2 == 0]
        a_odd.sort()
        a_even.sort(reverse=True)
        sorted_a = [0 for _ in range(n)]
        for v, i in zip(a_odd, a_odd_index):
            sorted_a[i] = v
        for v, i in zip(a_even, a_even_index):
            sorted_a[i] = v
        answers[x] = f'Case #{x + 1}: {" ".join(map(str, sorted_a))}'
    print(answers)