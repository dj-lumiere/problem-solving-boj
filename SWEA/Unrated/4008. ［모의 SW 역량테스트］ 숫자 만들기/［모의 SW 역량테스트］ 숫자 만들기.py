from itertools import combinations


INF = 10 ** 18
MOD = 1_000_000_000
t = int(input())
answers = []
for hh in range(t):
    n = int(input())
    ops = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    answer_min = INF
    answer_max = -INF
    for pluses in combinations(range(n - 1), ops[0]):
        next_ops = [i for i in range(n - 1) if i not in pluses]
        for minuses in combinations(next_ops, ops[1]):
            next_ops2 = [i for i in next_ops if i not in minuses]
            for times in combinations(next_ops2, ops[2]):
                divides = [i for i in next_ops2 if i not in times]
                op_order = ["" for _ in range(n - 1)]
                for i in pluses:
                    op_order[i] = "+"
                for i in minuses:
                    op_order[i] = "-"
                for i in times:
                    op_order[i] = "*"
                for i in divides:
                    op_order[i] = "/"
                answer_sub = 0
                for i, (op, (a, b)) in enumerate(zip(op_order, zip(numbers, numbers[1:]))):
                    if i != 0:
                        a = answer_sub
                    if op == "+":
                        answer_sub = a + b
                    if op == "-":
                        answer_sub = a - b
                    if op == "*":
                        answer_sub = a * b
                    if op == "/":
                        if a < 0:
                            answer_sub = -(-a // b)
                        else:
                            answer_sub = a // b
                answer_min = min(answer_sub, answer_min)
                answer_max = max(answer_sub, answer_max)
    answer = answer_max - answer_min
    answers.append(f"#{hh + 1} {answer}")
print(*answers, sep="\n")
