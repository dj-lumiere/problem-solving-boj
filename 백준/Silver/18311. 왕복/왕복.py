import os
from bisect import bisect_left

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
        k = int(input())
        course_length = [int(input()) for _ in range(n)]
        accumulate_course_length = [0]
        for j, v in enumerate(course_length):
            accumulate_course_length.append(accumulate_course_length[-1] + v)
        for j, v in enumerate(reversed(course_length)):
            if j == 0:
                accumulate_course_length[-1] += v
                continue
            accumulate_course_length.append(accumulate_course_length[-1] + v)
        answer = bisect_left(accumulate_course_length, k)
        if accumulate_course_length[answer] == k:
            answer += 1
        if answer >= n:
            answer = 2 * n - answer
        answers[i] = f"{answer}"
    # while True:
    #     n = int(input())
    #     if n == 0:
    #         break
    #     a = [int(input()) for _ in range(n)]
    #     answers.append("\n".join(map(str, reversed(a)))+"\n0")
    print(answers)