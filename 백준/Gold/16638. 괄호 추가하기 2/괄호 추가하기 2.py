from sys import stdout, stderr


def get_operation_priority(operator):
    if operator == "+" or operator == "-":
        return 0
    if operator == "*" or operator == "/":
        return 1
    return -1


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        s = list(input())
        ops = [j for j in s[1::2]]
        max_answer = -(2 ** 32)
        for mask in range(1 << (n // 2)):
            prior_op = [mask & (1 << i) != 0 for i in range(n // 2)]
            if any(i and j for i, j in zip(prior_op, prior_op[1:])):
                continue
            op_order = [get_operation_priority(op) + prior * 2 for op, prior in zip(ops, prior_op)]
            answer = -2 ** 32
            stack = []
            op_order_stack = []
            result = []
            for i, v in enumerate(s):
                if "0" <= v <= "9":
                    result.append(int(v))
                    continue
                while stack and op_order_stack[-1] >= op_order[(i - 1) // 2]:
                    result.append(stack.pop())
                    op_order_stack.pop()
                stack.append(v)
                op_order_stack.append(op_order[(i - 1) // 2])
            while stack:
                result.append(stack.pop())
                op_order_stack.pop()
            stack = []
            for i, v in enumerate(result):
                if isinstance(v, int):
                    stack.append(v)
                elif v == "+":
                    b, a = stack.pop(), stack.pop()
                    stack.append(a + b)
                elif v == "-":
                    b, a = stack.pop(), stack.pop()
                    stack.append(a - b)
                elif v == "*":
                    b, a = stack.pop(), stack.pop()
                    stack.append(a * b)
            answer = stack[0]
            max_answer = max(max_answer, answer)
    answers.append(f"{max_answer}")
print(*answers, sep="\n")
