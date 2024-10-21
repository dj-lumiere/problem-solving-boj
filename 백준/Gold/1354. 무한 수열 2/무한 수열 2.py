from sys import setrecursionlimit, stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    answers = []
    MERGE = 1
    SORT = 2
    for hh in range(1, t + 1):
        n = int(input())
        p = int(input())
        q = int(input())
        x = int(input())
        y = int(input())
        results = dict()
        THRESHOLD = 10 ** 6
        result_small = [0 for _ in range(THRESHOLD + 1)]
        result_small[0] = 1
        stack = [n]
        for i in range(1, THRESHOLD + 1):
            next_number1 = max(i // p - x, 0)
            next_number2 = max(i // q - y, 0)
            result_small[i] = result_small[next_number1] + result_small[next_number2]
        while stack:
            i = stack.pop()
            if i <= THRESHOLD:
                continue
            next_number1 = max(i // p - x, 0)
            next_number2 = max(i // q - y, 0)
            sub_result1 = -INF
            sub_result2 = -INF
            if next_number1 <= THRESHOLD:
                sub_result1 = result_small[next_number1]
            elif next_number1 in results:
                sub_result1 = results[next_number1]
            if next_number2 <= THRESHOLD:
                sub_result2 = result_small[next_number2]
            elif next_number2 in results:
                sub_result2 = results[next_number2]
            if (sub_result1 != -INF) and (sub_result2 != -INF):
                results[i] = sub_result1 + sub_result2
                continue
            if i in results:
                continue
            if i not in results:
                results[i] = 0
            stack.append(i)
            for z in {next_number1, next_number2}:
                stack.append(z)
        answer = answer = result_small[n] if n <= THRESHOLD else results[n]
        answers.append(answer)
    print(*answers, sep="\n")
