import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    MOD = 10 ** 9 + 7
    INF = 10 ** 18
    for h in range(t):
        n = int(input())
        answer = [0 for _ in range(1001)]
        answer[0] = answer[1] = 1
        for i in range(2, 1001):
            impossible_number = []
            for j in range(1, i // 2 + 1):
                if answer[i - j] * 2 - answer[i - 2 * j] > 0:
                    impossible_number.append(answer[i - j] * 2 - answer[i - 2 * j])
            impossible_number = sorted(set(impossible_number))
            possible_number = [True for _ in range(200)]
            possible_number[0] = False
            for number in impossible_number:
                if number >= 200:
                    continue
                possible_number[number] = False
            answer[i] = possible_number.index(True)
        answers[h] = f"{answer[n]}"
    print(answers)