from sys import stderr, stdout

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
    t = INF
    answers = []
    for hh in range(t):
        k = input()
        if k is None:
            break
        k = int(k)
        s = input()
        encrypted = []
        freq = [0] * 26
        window = []
        for i in range(len(s)):
            if i < k:
                encrypted.append(s[i])
                freq[ord(s[i]) - 97] += 1
                window.append(s[i])
            else:
                max_freq = -1
                chosen = 0
                for c in range(26):
                    if freq[c] > max_freq:
                        max_freq = freq[c]
                        chosen = c
                shift = chosen + 1
                shifted = chr(((ord(s[i]) - 97 + shift) % 26) + 97)
                encrypted.append(shifted)
                left_char = window.pop(0)
                freq[ord(left_char) - 97] -= 1
                window.append(s[i])
                freq[ord(s[i]) - 97] += 1
        answer = ''.join(encrypted)
        answers.append(f"{answer}")
    print(*answers, sep="\n")