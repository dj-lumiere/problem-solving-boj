from itertools import product

N, K = map(int, input().split())
A, B = [0], [0]
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
answers = []
for i in product(zip(A, B), repeat=K):
    current_carrot = 0
    s = 1
    for (a, b) in i:
        current_carrot -= a
        if current_carrot < 0:
            break
        if a == 0:
            current_carrot += s
        s += b
    else:
        answers.append(current_carrot)
print(max(answers))