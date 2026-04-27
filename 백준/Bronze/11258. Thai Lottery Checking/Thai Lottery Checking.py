import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 0
    answers = ["" for _ in range(t)]
    MOD = 10 ** 9 + 7
    INF = 10 ** 18
    for h in range(t):
        pass
    first = input().decode()
    first_prize = int(input())
    second1 = input().decode()
    second1_prize = int(input())
    second2 = input().decode()
    second2_prize = int(input())
    second3 = input().decode()
    second3_prize = int(input())
    second4 = input().decode()
    second4_prize = int(input())
    third = input().decode()
    third_prize = int(input())
    while True:
        answer = 0
        n = input().decode()
        if n == "-1":
            break
        if n == first:
            answer += first_prize
        if n.startswith(second1):
            answer += second1_prize
        elif n.startswith(second2):
            answer += second2_prize
        if n.endswith(second3):
            answer += second3_prize
        elif n.endswith(second4):
            answer += second4_prize
        if n.endswith(third):
            answer += third_prize
        answers.append(f"{answer}")
    print(answers)