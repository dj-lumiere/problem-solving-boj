from random import randint

m, n, q = map(int, input().split())
a = list(map(int, input().split()))
queries = [f"? {i} {i}" for i in range(1, m + 1)]
results = []
answers = [0 for _ in range(n)]
for q in queries:
    print(q, flush=True)
    results.append(int(input()))
for i, v in enumerate(results):
    answers[i] = v % a[i] + 1
for i in range(m, n):
    answers[i] = randint(1, a[i])
print(*(["!"] + answers), flush=True)