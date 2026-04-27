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
        n = int(input())
        a,b,c,d = (int(input()) for _ in range(4))
        s = input()
        if s.count("a")>a or s.count("b")>b or s.count("c")>c or s.count("d")>d:
            answer = "No"
        elif any(i==j for i,j in zip(s,s[1:])):
            answer = "No"
        elif s[0]!="a" or s[-1] != "a":
            answer = "No"
        else:
            answer = "Yes"
        answers.append(answer)
    print(*answers, sep="\n")