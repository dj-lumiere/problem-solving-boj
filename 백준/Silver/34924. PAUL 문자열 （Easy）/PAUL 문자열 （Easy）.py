from sys import stderr, stdout
 
with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
    INF = 10 ** 18
    MOD = 998_244_353
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        paul_string = input()
        p_index = paul_string.find("P")
        a_index = paul_string.find("A")
        u_index = paul_string.find("U")
        l_index = paul_string.find("L")
        if (l_index >= u_index >= a_index >= p_index and (a_index - p_index) % 2 == 1 and (u_index - a_index) % 2 == 1
                and (l_index - u_index) % 2 == 1 and (n - l_index) % 2 == 1 and p_index % 2 == 0):
            answers.append("YES")
        else:
            answers.append("NO")
    print(*answers, sep="\n")
