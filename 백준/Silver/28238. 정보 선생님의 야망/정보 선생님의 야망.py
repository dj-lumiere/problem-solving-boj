from sys import stdin
N = int(input())
class_availability = []
student_availability = [[0 for _ in range(5)] for _ in range(5)]
maximum_value = 0
maximum_index = [0, 1]
for _ in range(N):
    is_available = list(map(int, stdin.readline().strip().split(" ")))
    class_availability.append(is_available)
for i in range(5):
    for j in range(5):
        if i >= j:
            continue
        student_availability[i][j] = sum([k[i]==k[j]==1 for k in class_availability])
        if student_availability[i][j] > maximum_value:
            maximum_value = student_availability[i][j]
            maximum_index = [i, j]
print(maximum_value)
print(*[1 if i in maximum_index else 0 for i in range(5)])