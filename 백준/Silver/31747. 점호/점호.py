from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = 1
    answers = []
    for hh in range(t):
        n, k = int(input()), int(input())
        A = [int(input()) for _ in range(n)]
        student_index = {1: [i for i, v in enumerate(A) if v == 1], 2: [i for i, v in enumerate(A) if v == 2], }
        student_index[1].reverse()
        student_index[2].reverse()
        eprint(student_index)
        has_left = [False for _ in range(n)]
        left_students = 0
        last_index = k
        answer = 0
        while left_students < n:
            left_student_sub = 0
            if student_index[1]:
                last_one_index = student_index[1][-1]
                if last_one_index < last_index:
                    student_index[1].pop()
                    left_students += 1
                    left_student_sub += 1
                    has_left[last_one_index] = True
            if student_index[2]:
                last_two_index = student_index[2][-1]
                if last_two_index < last_index:
                    student_index[2].pop()
                    left_students += 1
                    left_student_sub += 1
                    has_left[last_two_index] = True
            answer += 1
            last_index += left_student_sub
        answers.append(f"{answer}")
    print(*answers, sep="\n")