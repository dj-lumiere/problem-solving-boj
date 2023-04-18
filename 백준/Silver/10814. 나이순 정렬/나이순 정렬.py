# 10814 나이순 정렬

N: int = int(input())
person_list: list[tuple[int, int, str]] = []
for i in range(N):
    age, name = input().split(" ")
    person_list.append((int(age), i, name))
person_list = sorted(person_list, key=lambda x: (x[0], x[1]))
print(*[f"{i} {j}" for (i, _, j) in person_list], sep="\n")
