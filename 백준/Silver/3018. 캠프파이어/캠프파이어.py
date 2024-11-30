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
        n, e = (int(input()) for _ in range(2))
        songs = [set() for _ in range(n + 1)]
        total_songs = 0
        for _ in range(e):
            k = int(input())
            people = [int(input()) for _ in range(k)]
            if 1 in people:
                total_songs += 1
                for p in people:
                    songs[p].add(total_songs)
            else:
                shared_songs = set()
                for p in people:
                    shared_songs.update(songs[p])
                for p in people:
                    songs[p].update(shared_songs)
        qualified = [str(p) for p in range(1, n + 1) if len(songs[p]) == total_songs]
        answer = '\n'.join(qualified)
        answers.append(f"{answer}")
    print(*answers, sep="\n")