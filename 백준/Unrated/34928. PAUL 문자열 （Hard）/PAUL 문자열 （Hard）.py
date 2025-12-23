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
        p_indices = [i for i, v in enumerate(paul_string) if v == "P"]
        a_indices = [i for i, v in enumerate(paul_string) if v == "A"]
        u_indices = [i for i, v in enumerate(paul_string) if v == "U"]
        l_indices = [i for i, v in enumerate(paul_string) if v == "L"]
        p_indices.sort()
        a_indices.sort()
        u_indices.sort()
        l_indices.sort()
        p_indices_even = [i for i in p_indices if i % 2 == 0]
        a_indices_odd = [i for i in a_indices if i % 2 == 1 and len(p_indices_even) >= 1 and i > p_indices_even[0]]
        u_indices_even = [i for i in u_indices if i % 2 == 0 and len(a_indices_odd) >= 1 and i > a_indices_odd[0]]
        l_indices_odd = [i for i in l_indices if i % 2 == 1 and len(u_indices_even) >= 1 and i > u_indices_even[0]]
        if (n % 2 == 0 and len(p_indices_even) >= 1 and len(a_indices_odd) >= 1 and len(u_indices_even) >= 1 and len(
                l_indices_odd) >= 1 and p_indices_even[0] < a_indices_odd[0] < u_indices_even[0] < l_indices_odd[-1]):
            answers.append("YES")
        else:
            answers.append("NO")
    print(*answers, sep="\n")
