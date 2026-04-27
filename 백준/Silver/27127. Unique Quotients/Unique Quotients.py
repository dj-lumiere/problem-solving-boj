from itertools import permutations

n=int(input())
answers = []
for i in permutations(range(10), r=5):
    j = [k for k in range(10) if k not in i]
    for j2 in permutations(j):
         i_int = int("".join(map(str, i)))
         j_int = int("".join(map(str, j2)))
         if i_int==j_int*9:
             answers.append((f"{i_int:0>5}", f"{j_int:0>5}"))
answers.sort(key=lambda x:x[0])
print(*answers[n-1])