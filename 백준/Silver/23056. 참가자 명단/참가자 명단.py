import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        m = int(input())
        blue_team = []
        white_team = []
        persons = [0 for _ in range(n + 1)]
        while True:
            class_number, name = int(input()), input().decode()
            if class_number == 0 and name == "0":
                break
            if class_number % 2 == 1 and persons[class_number] < m:
                blue_team.append((class_number, name))
                persons[class_number] += 1
            elif class_number % 2 == 0 and persons[class_number] < m:
                white_team.append((class_number, name))
                persons[class_number] += 1
        blue_team.sort(key=lambda x: (x[0], len(x[1]), x[1]))
        white_team.sort(key=lambda x: (x[0], len(x[1]), x[1]))
        blue_team.extend(white_team)
        answer = "\n".join(f"{x[0]} {x[1]}" for x in blue_team)
        answers[h] = f"{answer}"
    print(answers)