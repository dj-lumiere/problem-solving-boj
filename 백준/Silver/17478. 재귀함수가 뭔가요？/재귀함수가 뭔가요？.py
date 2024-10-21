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
    for hh in range(1, t + 1):
        n = int(input())
        a = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."
        b = '"재귀함수가 뭔가요?"'
        c = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
        d = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
        e = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
        f = '"재귀함수는 자기 자신을 호출하는 함수라네"'
        g = "라고 답변하였지."
        answers.append(a)
        stack = [0]
        while stack:
            i = stack.pop()
            if i == n:
                answers.extend(["_" * 4 * i + b, "_" * 4 * i + f])
            else:
                answers.extend(["_" * 4 * i + b, "_" * 4 * i + c, "_" * 4 * i + d, "_" * 4 * i + e])
                stack.append(i + 1)
        for i in reversed(range(n + 1)):
            answers.append("_" * 4 * i + g)
    print(*answers, sep="\n")
