# 5597 과제 안 내신 분..?

returned_assignment = [True] + [False] * 30
for _ in range(28):
    returned_assignment[int(input())] = True
for i in range(31):
    if not returned_assignment[i]:
        print(i)