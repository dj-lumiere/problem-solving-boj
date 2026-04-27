import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for a in range(t):
        n = int(input())
        t = int(input())
        finding_sign = int(input())
        sign_list = []
        for i in range(1, 1251):
            sign_list.extend([0, 1, 0, 1] + [0] * (i + 1) + [1] * (i + 1))
            if len(sign_list) > 30000:
                break
        zero_count_list = [-1] * 10001
        one_count_list = [-1] * 10001
        zero_count = 0
        one_count = 0
        for i, v in enumerate(sign_list):
            if v == 0 and zero_count <= 9999:
                zero_count += 1
                zero_count_list[zero_count] = i
            elif v == 1 and one_count <= 9999:
                one_count += 1
                one_count_list[one_count] = i
        if finding_sign == 0:
            answers[a] = f"{zero_count_list[t] % n}"
        elif finding_sign == 1:
            answers[a] = f"{one_count_list[t] % n}"
    print(answers)